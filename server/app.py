#!/usr/bin/env python3

# Imports the Flask class (and others) from the flask library.
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

# Creates an instance of the Flask application. __name__ tells Flask where to look for resources. appis the object used to configure routes and run the server.
app = Flask(__name__)

# The route decorator tells Flask: when someone visits this URL in the browser, run the function below.
@app.route('/contract/<int:id>')
def contract(id):    # defines a function named contract. Takes an argument (id) that Flask automatically passesfrom the route.
    return f'Contract ID: {id}'   # Returns a string response to the client

# The route decorator matches URLs with the name of a customer. Whatever comes after /customer/ is passed to the function as customer_name.
@app.route('/customer/<customer_name>')
def customer(customer_name):    # Defines a funciton for the /customer/ route. customer_name holds whatever is passed in the URL, e.g., Bob.
    return f'Customer Name: {customer_name}'    # Returns a string with the customer name.

if __name__ == '__main__':
    app.run(port=5555, debug=True)
