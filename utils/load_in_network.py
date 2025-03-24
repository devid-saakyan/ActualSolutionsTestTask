import os
import json
import multiprocessing
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (
    InNetwork, NegotiatedRate, NegotiatedRateProviderReference,
    NegotiatedPrice, ServiceCode, BillingCodeModifier
)

DATABASE_URL = "sqlite:///aetna.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine, expire_on_commit=False)

chunk_dir = ""
#chunk_files = sorted([f for f in os.listdir(chunk_dir) if f.startswith("in_network_chunk_") and f.endswith(".json")])
#total_chunks = len(chunk_files)

def process_chunk(args):
    file_index, file_name = args
    session = Session()
    filepath = os.path.join(chunk_dir, file_name)
    print(f"\n🚀 [{file_index+1}/2] PID {os.getpid()} обрабатывает {file_name}")


    with open(filepath, "r") as f:
        data = json.load(f)

    total_records = len(data)
    print(f"📦 В {file_name}: {total_records} записей")

    for i, item in enumerate(data, start=1):
        in_network = InNetwork(
            negotiation_arrangement=item["negotiation_arrangement"],
            name=item["name"],
            billing_code_type=item["billing_code_type"],
            billing_code_type_version=item["billing_code_type_version"],
            billing_code=item["billing_code"],
            description=item["description"]
        )
        session.add(in_network)
        session.flush()

        for rate in item.get("negotiated_rates", []):
            negotiated_rate = NegotiatedRate(in_network_id=in_network.id)
            session.add(negotiated_rate)
            session.flush()

            for ref_id in rate.get("provider_references", []):
                session.add(NegotiatedRateProviderReference(
                    negotiated_rate_id=negotiated_rate.id,
                    reference_id=ref_id
                ))

            for price in rate.get("negotiated_prices", []):
                negotiated_price = NegotiatedPrice(
                    negotiated_rate_id=negotiated_rate.id,
                    negotiated_type=price["negotiated_type"],
                    negotiated_rate=float(price["negotiated_rate"]),
                    expiration_date=price["expiration_date"],
                    billing_class=price.get("billing_class")
                )
                session.add(negotiated_price)
                session.flush()

                for code in price.get("service_code", []):
                    session.add(ServiceCode(
                        negotiated_price_id=negotiated_price.id,
                        code=code
                    ))

                for mod in price.get("billing_code_modifier", []):
                    session.add(BillingCodeModifier(
                        negotiated_price_id=negotiated_price.id,
                        modifier=mod
                    ))
        if i % 10 == 0 or i == total_records:
            print(f"📊 [{file_name}] Обработано {i}/{total_records} записей")
    session.commit()
    session.close()


def run_parallel_load(files=None, num_workers=2):
    files = files #or chunk_files
    tasks = list(enumerate(files))
    with multiprocessing.Pool(processes=num_workers) as pool:
        pool.map(process_chunk, tasks)

if __name__ == '__main__':
    run_parallel_load(['in_network_chunk_1.json', 'in_network_chunk_2.json'])
