
from flask import Flask, jsonify, request
from flask_cors import CORS

from .models.model import engine, Base, Session
from .models.customer import Customer, CustomerSchema
from .models.loan import Loan, LoanSchema


app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/customers', methods=['GET'])
def get_customers():

    # fetching from the database
    session = Session()
    schema = CustomerSchema(many=True)

    if request.args.get("name") != None:
        customer_objects = session.query(Customer) \
        .filter(Customer.name.ilike('%' + request.args.get("name") + '%')) \
        .all()

        customers = schema.dump(customer_objects)
        session.close()
        return jsonify(customers)



    customer_objects = session.query(Customer).all()
    customers = schema.dump(customer_objects)

    # serializing as JSON
    session.close()
    return jsonify(customers)

@app.route('/loans', methods=['GET'])
def search_loans_by_customer():

    if request.args.get("customerId") != None:
        session = Session()
        customer_loans_objs = session.query(Loan) \
        .join(Customer) \
        .filter(Loan.customer_id == request.args.get("customerId")) \
        .all()

        schema = LoanSchema(many=True)
        customer_loans = schema.dump(customer_loans_objs)

        session.close()
        return jsonify(customer_loans)
