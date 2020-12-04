from sqlalchemy import Column, String, DateTime
from marshmallow import Schema, fields

from .model import Model, Base

class Customer(Model, Base):
    __tablename__ = 'customers'

    name = Column(String(100), nullable=False) 
    phone_number = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    location = Column(String(20), nullable=False)
    region = Column(String(20), nullable=False)
    coordinates = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


    def __init__(self, name, phone_number, city, location, region, coordinates):
        Model.__init__(self)
        self.name = name
        self.phone_number = phone_number
        self.city = city
        self.location = location
        self.region = region
        self.coordinates = coordinates
    
    def __repr__(self):
        return '<Customer(name={self.phone_number!r})>'.format(self=self)

class CustomerSchema(Schema):
    name = fields.Str()
    phone_number = fields.Str()
    city = fields.Str()
    location = fields.Str()
    region = fields.str()
    coordinates = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()