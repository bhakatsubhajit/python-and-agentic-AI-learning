# basic calculator ask users for the operation and 2 numbers and display result

firstNum = int(input("Enter your first number: "))
secondNum = int(input("Enter your second number: "))

operatorInput = input("choose operation symbol(+,-,*,/) : ")

match operatorInput:

    case '+':
        result = int(firstNum+secondNum)
    case '-':
        result = int(firstNum-secondNum)
    case '*':
        result = int(firstNum*secondNum)
    case '/':
        result = int(firstNum/secondNum)
    case _:
        print("invalid operator")

print("the result is :",result)


