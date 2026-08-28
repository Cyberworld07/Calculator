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
    print ("---Calculator---")
    print ("Select operation: ")
    print("1. Add")
    print ("2.Subtract")