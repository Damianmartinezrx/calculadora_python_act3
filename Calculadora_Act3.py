def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b
def division (a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division en zero."


num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

operation = input("Que operacion? (+, -, *, /): ")

if operation == '+':
    result = suma(num1, num2)
elif operation == '-':
    result = resta(num1, num2)   
elif operation == '*':
    result = multiplicacion(num1, num2)
elif operation == '/':
    result = division(num1, num2)
else:
    result = "Operacion no valida."
    

print("El resultado es:", result)