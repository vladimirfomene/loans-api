from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from marshmallow import Schema, fields

from .model import Model, Base


class Loan(Model, Base):
    __tablename__ = 'loans'

    
    loan_amount = Column(Integer)
    amount_repaid = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    customer = relationship('Customer', backref=backref('loans', lazy=True))

    def __init__(self, loan_amount, amount_repaid, created_at, updated_at, customer):
        self.loan_amount = loan_amount
        self.amount_repaid = amount_repaid
        self.created_at = created_at
        self.updated_at = updated_at
        self.customer = customer

    def __repr__(self):
        return '<Loan(name={self.loan_amount!r})>'.format(self=self)


class LoanSchema(Schema):
    id = fields.Number()
    loan_amount = fields.Number()
    amount_repaid = fields.Number()
    customer_id = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()