from fastapi import FastAPI
from routers import (
    provider_group,
    npi,
    provider_reference,
    negotiated_price,
    service_code,
    billing_code_modifier,
    negotiated_rate,
    negotiated_rate_provider_reference,
    in_network,
)

app = FastAPI(
    title="Aetna API",
    description="API for working with Aetna database tables",
    version="1.0.1",
)

app.include_router(provider_group.router)
app.include_router(npi.router)
app.include_router(provider_reference.router)
app.include_router(negotiated_price.router)
app.include_router(service_code.router)
app.include_router(billing_code_modifier.router)
app.include_router(negotiated_rate.router)
app.include_router(negotiated_rate_provider_reference.router)
app.include_router(in_network.router)

@app.get("/")
def read_root():
    return {"message": "Aetna API is running"}
