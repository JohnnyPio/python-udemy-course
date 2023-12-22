#Calculator 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Pick first num
num1 = int(input("What's the first number?: "))

#Pick operator
for operators in operations:
    print(operators)
operation_symbol = input("Pick an operation from the line above: ")

#Get dictionary key
operator = operations[operation_symbol]

#Pick second num
num2 = int(input("What's the second number?: "))

#Do Math based on operator and numbers
answer = operator(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")