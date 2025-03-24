import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, ProviderReference, ProviderGroup, NPI

engine = create_engine("sqlite:///aetna.db")
Session = sessionmaker(bind=engine)
session = Session()

with open("provider_references.json", "r") as f:
    data = json.load(f)

for item in data:
    provider_ref = ProviderReference(provider_group_id=item["provider_group_id"])
    session.add(provider_ref)
    session.flush()

    for group in item["provider_groups"]:
        provider_group = ProviderGroup(
            provider_reference_id=provider_ref.id,
            tin_type=group["tin"]["type"],
            tin_value=group["tin"]["value"]
        )
        session.add(provider_group)
        session.flush()

        for npi_value in group["npi"]:
            npi = NPI(
                provider_group_id=provider_group.id,
                value=str(npi_value)
            )
            session.add(npi)

session.commit()
session.close()