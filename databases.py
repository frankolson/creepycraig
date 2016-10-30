#
# File for the databases setup
#
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

## setup SQLite engines
apartment_engine = create_engine('sqlite:///apartment_listings.db', echo=False)
car_engine = create_engine('sqlite:///car_listings.db', echo=False)
Base = declarative_base()

## ApartmentListing DB Model
class ApartmentListing(Base):
    __tablename__ = 'apartment_listings'

    id        = Column(Integer, primary_key=True)
    area      = Column(String)
    bart_dist = Column(Float)
    bart_stop = Column(String)
    cl_id     = Column(Integer, unique=True)
    created   = Column(DateTime)
    latitutde = Column(Float)
    link      = Column(String, unique=True)
    location  = Column(String)
    longitude = Column(Float)
    name      = Column(String)
    near_bart = Column(Boolean)
    price     = Column(Float)

## CarListing DB Model
class CarListing(Base):
    __tablename__ = 'car_listings'

    id        = Column(Integer, primary_key=True)
    area      = Column(String)
    cl_id     = Column(Integer, unique=True)
    created   = Column(DateTime)
    link      = Column(String, unique=True)
    location  = Column(String)
    name      = Column(String)
    price     = Column(Float)

## Create teh db sessions
Base.metadata.create_all(apartment_engine)
Base.metadata.create_all(car_engine)

ApartmentSession = sessionmaker(bind=apartment_engine)
CarSession = sessionmaker(bind=apartment_engine)
apartment_session = ApartmentSession()
car_session = CarSession()
