# https://youtu.be/eX5gzivYyIQ <- Video tutorial for this code

# Operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not possible."
    return a / b

def calculator():
    print("Welcome to the simple calculator!")
    print("Type quit to exit.")
    
    while True:
        num1 = input("Enter the first number: ")
        if num1.lower() == 'quit':
            break
        num2 = input("Enter the second number: ")
        if num2.lower() == 'quit':
            break
        operator = input("Enter the operator (+, -, *, /): ")
        if operator.lower() == 'quit':
            break
        
        try: 
            num1 = float(num1)
            num2 = float(num2)
        except:
            print("Invalid input. Please enter numbers.")
            continue
        
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please enter +, -, *, or /.")
            continue

        print(f"The result is: {result}")
        
calculator()