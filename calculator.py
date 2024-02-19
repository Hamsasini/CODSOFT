def display():
    print("\nSimple Calculator")
    print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Remainder \n6.Power  \n7.Root \n8.Exit")
    try:
        ch = int(input("Enter choice from 1 to 8: "))
        return ch
    except ValueError as e:
        print("Invalid choice. Enter a valid choice.")
        return display()

def Input_1():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError as e:
        print("Invalid value. Please enter numeric values.")
        return Input_1()

def Input_2():
    try:
        a = float(input("Numerator: "))
        b = float(input("Denominator: "))
        return a, b
    except ValueError as e:
        print("Invalid value. Please enter numeric values.")
        return Input_2()

def Input_3():
    try:
        a = float(input("Enter base number: "))
        b = float(input("Enter exponent number: "))
        return a, b
    except ValueError as e:
        print("Invalid value. Please enter numeric values.")
        return Input_3()

def add(a,b):
    print(a, "+", b, "=", a + b)

def subtract(a, b):
    print(a, "-", b, "=", a - b)

def multiply(a, b):
    print(a, "*", b, "=", a * b)

def divide(a, b):
    try:
        print(a, "/", b, "=", a / b)
    except ZeroDivisionError as e:
        del a, b
        print("Division by zero is not possible. Please enter other possible integers.")
        return Input_2()

def remainder(a, b):
    print(a, "%", b, "=", a % b)

def power(a, b):
    print(a, "^", b, "=", a ** b)

def root():
    a=float(input("Enter base number:"))
    b=float(input("Enter root number:"))
    if b == 2:
        print("Square root of", a, "=", a ** (1 / b))
    elif b == 3:
        print("Cube root of", a, "=", a ** (1 / b))
    else:
        print(b, "th root of", a, "=", a ** (1 / b))

while True:
    choice=display()
    if choice == 1:
        a, b = Input_1()
        add(a,b)
    elif choice == 2:
        a, b = Input_1()
        subtract(a, b)
    elif choice == 3:
        a, b = Input_1()
        multiply(a, b)
    elif choice == 4:
        a, b = Input_2()
        divide(a, b)
    elif choice == 5:
        a, b = Input_2()
        remainder(a, b)
    elif choice == 6:
        a, b = Input_3()
        power(a, b)
    elif choice == 7:
        root()
    elif choice == 8:
        print("Exit")
        
    else:
        print("Invalid choice. Please enter a valid choice.")

    proceed=str(input("Do you want to continue?(yes/no)"))
    if proceed!="yes":
        break
    



1