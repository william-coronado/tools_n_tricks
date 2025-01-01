"""Exploring alternative methods for control flow in Python for building a calculator."""
import operator

option = input("""Enter option to test control flow technique...
    1. Using the operator Module
    2. Using eval() for Dynamic Evaluation
    3. Using match and case
    4. Dictionary Dispatch
    5. Lambda Functions
    6. Object-Oriented Approach
    7. Function Mapping
    
    """)

match option:
    case "1":
        print("Using the operator Module")
        # 1. Using the operator Module
        action = {
            "+" : operator.add,
            "-" : operator.sub,
            "/" : operator.truediv,
            "*" : operator.mul,
            "**" : pow  # Power operator
        }

        print(action['/'](37, 5))  # Output: 7.4
    case "2":
        print("Using eval() for Dynamic Evaluation")
        # 2. Using eval() for Dynamic Evaluation
        def calculator(a, b, operation):
            return eval(f"{a} {operation} {b}")
        
        print(calculator(37, 5, '/'))  # Output: 7.4
        
    case "3":
        print("Using match and case")
        # 3. Using match and case
        def calculator(a, b, operation):
            match operation:
                case '+':
                    return a + b
                case '-':
                    return a - b
                case '*':
                    return a * b
                case '/':
                    return a / b
                case _:
                    return "Invalid operation"

        print(calculator(37, 5, '/'))  # Output: 7.4
        
    case "4":
        print("Dictionary Dispatch")
        # 4. Dictionary Dispatch
        def add(x, y): return x + y
        def subtract(x, y): return x - y
        def multiply(x, y): return x * y
        def divide(x, y): return x / y

        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }

        operation = input("Enter operation (+, -, *, /): ")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        result = operations[operation](x, y)
        print(result)
        
    case "5":
        print("Lambda Functions")
        # 5. Lambda Functions
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

        operation = input("Enter operation (+, -, *, /): ")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        result = operations[operation](x, y)
        print(result)
        
    case "6":
        print("Object-Oriented Approach")
        # 6. Object-Oriented Approach
        class Calculator:
            def add(self, x, y): return x + y
            def subtract(self, x, y): return x - y
            def multiply(self, x, y): return x * y
            def divide(self, x, y): return x / y

        calc = Calculator()
        operations = {
            '+': calc.add,
            '-': calc.subtract,
            '*': calc.multiply,
            '/': calc.divide
        }

        operation = input("Enter operation (+, -, *, /): ")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        result = operations[operation](x, y)
        print(result)
        
    case "7":
        print("Function Mapping")
        # 7. Function Mapping
        def calculate(operation, x, y):
            return {
                '+': x + y,
                '-': x - y,
                '*': x * y,
                '/': x / y
            }.get(operation, "Invalid operation")

        operation = input("Enter operation (+, -, *, /): ")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        result = calculate(operation, x, y)
        print(result)
        
    case _:
        print("Invalid option")














