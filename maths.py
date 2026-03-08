#Library needed 
import math

#The mathamatical operations that can be done 
def addition(value):
    number = float(input("Enter the next number: "))
    return value + number

def subtraction(value):
    number = float(input("Enter the next number: "))
    return value - number

def multiplication(value):
    number = float(input("Enter the next number: "))
    return value * number

def division(value):
    number = float(input("Enter the next number: "))
    if number == 0:
        print("Error: Cannot divide by zero.")
        return value
    return value / number

def power(value):
    number = float(input("Enter the exponent: "))
    return value ** number

def modulus(value):
    number = float(input("Enter the next number: "))
    if number == 0:
        print("Error: Cannot do modulus by zero.")
        return value
    return value % number


def square_root(value):
    if value < 0:
        print("Error: Cannot find square root of a negative number.")
        return value
    return math.sqrt(value)

#Opening to the calculator 
print("Simple Calculator")
print("Available operations: +  -  *  /  ^  %  sqrt  reset  exit")

value = float(input("Enter the starting number: "))

#Loop until the user is done with the operations 
while True:
    operation = input("Choose an operation: ").lower()

    #Loops with error handling 
    if operation == "+":
        value = addition(value)
    elif operation == "-":
        value = subtraction(value)
    elif operation == "*":
        value = multiplication(value)
    elif operation == "/":
        value = division(value)
    elif operation == "^":
        value = power(value)
    elif operation == "%":
        value = modulus(value)
    elif operation == "sqrt":
        value = square_root(value)
    elif operation == "reset":
        value = float(input("Enter a new starting number: "))
    elif operation == "exit":
        break
    else:
        print("Invalid operation. Please try again.")
        continue
    #sub total adding 
    print("Current value:", value)
#final total adding 
print("Final value:", value)
