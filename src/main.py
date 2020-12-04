
from flask import Flask, jsonify, request
from flask_cors import CORS

from .models.model import engine, Base, Session
from .models.customer import Customer, CustomerSchema
from .models.loan import Loan, LoanSchema


app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/customers')
def get_customers():

    # fetching from the database
    session = Session()
    customer_objects = session.query(Customer).all()

    # transforming into JSON-serializable objects
    schema = CustomerSchema(many=True)
    customers = schema.dump(customer_objects)

    # serializing as JSON
    session.close()
    return jsonify(customers.data)

@app.route('/customers/<id>')
def search_customers():
