from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:my_string>')
def print_string(my_string):
    print(my_string)  # Print the string to the console
    return f'Printed String: {my_string}'  # Display it in the web browser

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(1, num + 1))
    return f'Counting Numbers:\n{numbers}'

@app.route('/math/<int:num1><string:operation><int:num2>')
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
            return 'Error: Division by zero is not allowed.'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation.'

    return f'Result of {num1} {operation} {num2} is: {result}'

if __name__ == '__main__':
    app.run(port=5555,debug=True)

