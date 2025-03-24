from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class ProviderGroup(Base):
    __tablename__ = 'provider_groups'
    id = Column(Integer, primary_key=True)
    provider_reference_id = Column(Integer, ForeignKey('provider_references.id'))
    tin_type = Column(String)
    tin_value = Column(String)

    npi_values = relationship("NPI", back_populates="provider_group")
    provider_reference = relationship("ProviderReference", back_populates="provider_groups")


class NPI(Base):
    __tablename__ = 'npi'
    id = Column(Integer, primary_key=True)
    provider_group_id = Column(Integer, ForeignKey('provider_groups.id'))
    value = Column(String)

    provider_group = relationship("ProviderGroup", back_populates="npi_values")


class ProviderReference(Base):
    __tablename__ = 'provider_references'
    id = Column(Integer, primary_key=True)
    provider_group_id = Column(Integer)

    provider_groups = relationship("ProviderGroup", back_populates="provider_reference")


class NegotiatedPrice(Base):
    __tablename__ = 'negotiated_prices'
    id = Column(Integer, primary_key=True)
    negotiated_rate_id = Column(Integer, ForeignKey('negotiated_rates.id'))
    negotiated_type = Column(String)
    negotiated_rate = Column(Float)
    expiration_date = Column(String)
    billing_class = Column(String)

    negotiated_rate_parent = relationship("NegotiatedRate", back_populates="negotiated_prices")
    service_codes = relationship("ServiceCode", back_populates="negotiated_price")
    billing_code_modifiers = relationship("BillingCodeModifier", back_populates="negotiated_price")


class ServiceCode(Base):
    __tablename__ = 'service_codes'
    id = Column(Integer, primary_key=True)
    negotiated_price_id = Column(Integer, ForeignKey('negotiated_prices.id'))
    code = Column(String)

    negotiated_price = relationship("NegotiatedPrice", back_populates="service_codes")


class BillingCodeModifier(Base):
    __tablename__ = 'billing_code_modifiers'
    id = Column(Integer, primary_key=True)
    negotiated_price_id = Column(Integer, ForeignKey('negotiated_prices.id'))
    modifier = Column(String)

    negotiated_price = relationship("NegotiatedPrice", back_populates="billing_code_modifiers")


class NegotiatedRate(Base):
    __tablename__ = 'negotiated_rates'
    id = Column(Integer, primary_key=True)
    in_network_id = Column(Integer, ForeignKey('in_network.id'))

    provider_references = relationship("NegotiatedRateProviderReference", back_populates="negotiated_rate")
    negotiated_prices = relationship("NegotiatedPrice", back_populates="negotiated_rate_parent")
    in_network = relationship("InNetwork", back_populates="negotiated_rates")


class NegotiatedRateProviderReference(Base):
    __tablename__ = 'negotiated_rate_provider_references'
    id = Column(Integer, primary_key=True)
    negotiated_rate_id = Column(Integer, ForeignKey('negotiated_rates.id'))
    reference_id = Column(Integer)

    negotiated_rate = relationship("NegotiatedRate", back_populates="provider_references")


class InNetwork(Base):
    __tablename__ = 'in_network'
    id = Column(Integer, primary_key=True)
    negotiation_arrangement = Column(String)
    name = Column(String)
    billing_code_type = Column(String)
    billing_code_type_version = Column(String)
    billing_code = Column(String)
    description = Column(String)

    negotiated_rates = relationship("NegotiatedRate", back_populates="in_network")


if __name__ == '__main__':
    #engine = create_engine("postgresql://aetna:11111111@localhost:5432/aetna")
    engine = create_engine("sqlite:///aetna.db")
    Base.metadata.create_all(engine)
    print("db created")