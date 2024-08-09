# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a + b)

@app.route('/sub')
def subtract():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a - b)

@app.route('/mult')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a * b)

@app.route('/div')
def divide():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a / b)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def math_opers(oper):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operators[oper](a, b))