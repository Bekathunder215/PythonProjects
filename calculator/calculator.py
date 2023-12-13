#this is a basic calculator app

def add():
    a = int(input("Give me A's value: "))
    b = int(input("Give me B's value: "))
    return print(f"{a} + {b} = {(a + b)}")

def subtract():
    a = int(input("Give me A's value: "))
    b = int(input("Give me B's value: "))
    return print(f"{a} - {b} = {(a - b)}")

def div():
    a = int(input("Give me A's value: "))
    b = int(input("Give me B's value: "))
    return print(f"{a} / {b} = {(a / b)}")

def mult():
    a = int(input("Give me A's value: "))
    b = int(input("Give me B's value: "))
    return print(f"{a} * {b} = {(a * b)}")

quit = False
print("-----------------------------------")
print("Welcome to a simple calculator!!")

while not quit:
    print("-----------------------------------------")
    print("Please select the desired calculation")
    print("A for Addition\nB for Subtraction\nC for division\nD for Multiplication\nQ for quiting")
    user = input("Your choice: ").lower()
    match user:
        case 'a':
            print("-----------------------------------------")
            add()        
        case 'b':
            print("-----------------------------------------")
            subtract()        
        case 'c':
            print("-----------------------------------------")
            div()        
        case 'd':
            print("-----------------------------------------")
            mult()  
        case 'q':
            quit = True      
        case _:
            print("Invalid input! Try Again.")
            continue
print("-----------------------------------------")
print("G-O-O-D ------ B-Y-E-!")

