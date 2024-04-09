import math
print("Welcome to the calculator!!!")
print("This is a calculator that includes addition, subtraction, multiplication, division and square root")
print ("The following signs will be the one you need for the calculator: + for addition, - for subtraction, * for multiplication, / for division, sqrt for square root)")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero not posible, division by zero has no meaning, rookie error"
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number. Cmon, no rookie error, no more"
    else:
        return math.sqrt(x)

# Input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter the operator")

# Perform the operation based on the input
if operator == '+':
    print("Result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
elif operator == 'sqrt':
    print("Result:", square_root(num1))
else:
    print("Invalid operator!")