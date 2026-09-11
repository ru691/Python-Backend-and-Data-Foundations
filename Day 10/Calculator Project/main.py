import art
print(art.logo)



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }

def calculator():
    n1 = float(input("Enter the first number: "))
    while True:
        for symbol in operations:
            print(symbol)
        operator = input("Enter the operator: ")
        n2 = float(input("Enter the second number: "))
        calculation = operations[operator]
        answer = calculation(n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")
        choice = input("Do you want to continue? (y/n): ")
        if choice == "y":
            n1 = answer
        else :
            n1 = float(input("Enter the first number: "))
calculator()