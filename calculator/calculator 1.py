# calculator
def add(a,b):
    return a + b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error:division by zero"
    return a/b
while True:
    print("---Calculator---")
    print("Select operation: ")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.exist")
    choice = int(input("Enter choice(1/2/3/4/5): "))
    if choice == 5:
        print("Calculator closed")
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 1:
        print("Result:",add(a,b))
    elif choice == 2:
        print("Result:",subtract(a,b))
    elif choice == 3:
        print("Result:",multiply(a,b))
    elif choice == 4:
        if b == 0:
            print("Error")
        else:
            print("Result:",divide(a,b))
    else:
        print("Invalid choice!")


