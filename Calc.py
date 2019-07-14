print("Calculator")


# Adding
def Add(x, y):
    print(int(x + y))


# Sub
def Sub(x, y):
    print(int(x - y))


# Muli
def Multi(x, y):
    print(int(x * y))


# Dividing
def Div(x, y):
    print(int(x / y))


# Printing
def Printing(x):
    print("The total is" + x)


# Calculations
def Calc(userinput, x, y):
    if userinput == 1:
        Add(x, y)
    elif userinput == 2:
        Sub(x, y)
    elif userinput == 3:
        Multi(x, y)
    elif userinput == 4:
        Div(x, y)
    else:
        print("Wrong input")
        Choices()


# Choices
def Choices():
    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number: "))
    print("Please pick a option 1 - 4")
    print("1.) Adding")
    print("2.) Subtraction")
    print("3.) Mulipcation")
    print("4.) Dividing")
    userinput = int(input("What is your choice? "))
    Calc(userinput, num1, num2)


Choices()
