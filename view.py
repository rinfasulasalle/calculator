# view.py

from flask import Flask, render_template, request
from presenter import CalculatorPresenter

app = Flask(__name__)
presenter = CalculatorPresenter(app)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.form['a']
    b = request.form['b']
    operation = request.form['operation']
    result = presenter.calculate(operation, a, b)
    return render_template('calculator.html', result=result)
