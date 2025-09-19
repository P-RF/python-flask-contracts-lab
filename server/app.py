#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route('/contract/<int:id>') # Route decorator is used to handle a request for a dynamic URL. 
def contract(id): 
    for contract in contracts:  # For loop iterates over the contracts list.
        if contract['id'] == id:    # Checks if the contract's id matches the id from the URL.
            return contract["contract_information"], 200    # Returns a response to the client.
    return '404: Contract not found', 404   # Handles the case if no contract is found.

@app.route('/customer/<customer_name>') # Route decorator is used to handle a request to URLs that match /customer/<customer_name>. 
def customer(customer_name):
    if customer_name.lower() in [customer.lower() for customer in customers]:   # Checks if the provided name exists in the customers list (case-sensitive).
        return '', 204  # Runs an empty response with status code 204.
    else:
        return '404: Customer not found', 404   # Handles the case where a customer is not found.

if __name__ == '__main__':
    app.run(port=5555, debug=True)
