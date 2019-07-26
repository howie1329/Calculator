print("Calculator")


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


# Calculations
def calc(userinput, x, y):
    if userinput == 1:
        add(x, y)
    elif userinput == 2:
        sub(x, y)
    elif userinput == 3:
        multi(x, y)
    elif userinput == 4:
        div(x, y)
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
    print("3.) Mulipcation")
    print("4.) Dividing")
    user_input = int(input("What is your choice? "))
    calc(user_input, num1, num2)


choices()
