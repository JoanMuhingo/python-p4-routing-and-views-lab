#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    if parameter == 'hello':
        print(parameter)
        return 'hello'
    else:
        print(parameter)
        return f'<h2>Printed String: {parameter}</h2>'

@app.route('/count/<int:parameter>')
def count(parameter):
    if parameter >= 0:
        numbers ='\n'.join(map(str, range(parameter + 1)))
        return f'Count from 0 to {parameter}:\n{numbers}\n'
    else:
        return 'Parameter must be a non-negative integer\n'    

@app.route('/math/float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2    
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'    
    elif operation == '%':
        result = num1 % num2  
    else:
        return 'Invalid operation'
    return f'<h2>Result: {result}</h2>'    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
