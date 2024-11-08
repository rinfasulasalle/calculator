# presenter.py

from model import CalculatorModel

class CalculatorPresenter:
    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel()

    def calculate(self, operation, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return "Entrada no válida, ingrese números válidos."
        
        if operation == 'add':
            result = self.model.add(a, b)
        elif operation == 'subtract':
            result = self.model.subtract(a, b)
        elif operation == 'multiply':
            result = self.model.multiply(a, b)
        elif operation == 'divide':
            try:
                result = self.model.divide(a, b)
            except ValueError as e:
                return str(e)
        else:
            return "Operación no válida."

        return f"El resultado es: {result}"
