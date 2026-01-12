# Task 1: Simple Calculator:
# Description: Develop a basic calculator that can
# perform four primary arithmetic operations: addition,
# subtraction, multiplication, and division.

# Objectives:
# a. Create functions for each operation.
# b. Take two inputs from the user and allow them to select
# the desired operation.
# c. Handle division by zero with appropriate error
# messages.

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    else:
        print("Invalid input")

def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The sum is: {a + b}")

def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The difference is: {a - b}")

def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The product is: {a * b}")

def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print(f"The quotient is: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    calculator()