# Created and Finished by Howard Thomas


calculator_usage = "yes"


# Adding
def add(x, y):
    print(int(x + y))


# Sub
def sub(x, y):
    print(int(x - y))


# Multi
def multi(x, y):
    print(int(x * y))


# Dividing
def div(x, y):
    print(int(x / y))


# Printing
def printing(x):
    print("The total is" + x)


def heading():
    print("Calculator")
    print("Created by Howard Thomas in python")


def start():
    global calculator_usage
    heading()
    while calculator_usage == "yes":
        calculator_usage = input("Would you like to use the calculator? (yes/no) ")
        choices()
        calculator_usage = input("would you like to use the calculator again? (yes/no) ")


# Calculations
def calc(user_input, num1, num2):
    if user_input == 1:
        add(num1, num2)
    elif user_input == 2:
        sub(num1, num2)
    elif user_input == 3:
        multi(num1, num2)
    elif user_input == 4:
        div(num1, num2)
    else:
        print("Wrong input")
        choices()


# Choices
def choices():
    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number: "))
    print("Please pick a option 1 - 4")
    print("1.) Adding")
    print("2.) Subtraction")
    print("3.) Multiplication")
    print("4.) Dividing")
    user_input = int(input("What is your choice? "))
    calc(user_input, num1, num2)


if __name__ == "__main__":
    start()
