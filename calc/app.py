# Put your app in here.
# Build a simple calculator with Flask, which uses URL query parameters to 
# get the numbers to calculate with.

# Make a Flask app that responds to 4 different routes. Each route does a math operation
# with two numbers, a*** and ***b***, which will be passed in as URL GET-style query parameters.

# ***/add***   Adds ***a*** and ***b*** and returns result as the body.

# ***/sub***   Same, subtracting ***b*** from ***a***.

# ***/mult***   Same, multiplying ***a*** and ***b***.

# ***/div***   Same, dividing ***a*** by ***b***.

# For example, a URL like ***http://localhost:5000/add?a=10&b=20*** should 
# return a string response of exactly **30**.

# Write the routes for this but **don’t hardcode the math operation 
# in your route function** directly. Instead, we’ve provided helper
# functions for this in the file ***operations.py***:

from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add/<int:id1>/<int:id2>')
def adder(id1, id2):
    """Add two numbers together and give sum"""
    addition = add(id1, id2)
    return f"<h1>The calculated sum is: {addition}</h1>"

@app.route('/subtract/<int:id1>/<int:id2>')
def subtract(id1, id2):
    """Subtract two numbers and give difference"""
    difference = sub(id1, id2)
    return f"<h1>The calculated difference is: {difference}</h1>"

@app.route('/mult/<int:id1>/<int:id2>')
def multiply(id1, id2):
    """Multiply two numbers and give product"""
    product = mult(id1, id2)
    return f"<h1>The calculate product is: {product}</h1>"

@app.route('/div/<int:id1>/<int:id2>')
def division(id1, id2):
    """Divide two numbers and give quotient"""
    quotient = div(id1, id2)
    return f"<h1>The calculate quotient is: {quotient}</h1>"

operations = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

if __name__ == '__main__':
    app.run(debug=True, port=4000)


