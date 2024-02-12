import art
print(art.logo)
def calculation(operation_symbol, answear, num3):
    calculator_function = operations[operation_symbol]
    return calculator_function(answear, num3)
def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def muliplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : substract,
    "*" : muliplication,
    "/" : division
}
def calculato():
    num1 = float(input("What its the first nummber?"))
    for operator in operations:
        print(operator)
    operation_symbol = input("Pick a operator from the line above: ")
    num2 = float(input("What is the second nummber?"))
    calculator_function = operations[operation_symbol]
    answear = calculator_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answear}")
    shut_down_repuest = input(f"Do you want to continue calculating with {answear}, y/n")
    while shut_down_repuest != "n":
        old_answear = answear
        for operator in operations:
            print(operator)
        operation_symbol = input("Pick a operator from the line above: ")
        num3 = float(input("What the second nummber?"))
        answear = calculation(operation_symbol, answear, num3)
        print(f"{old_answear} {operation_symbol} {num3} = {answear}")
        shut_down_repuest = input(f"Do you want to continue calculating with {answear}, y/n")
    calculato()
calculato()



