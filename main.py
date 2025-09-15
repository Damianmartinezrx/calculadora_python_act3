def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b
def division (a, b):
    return a / b

def menu():
    print("Bienvenido a la calculadora  simple  en Python\n")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Salir")    

def main(): 
    while True:
        menu()
        try:    
            option = int(input("\nSeleccione una opcion (1-5): "))
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))          
            match option:
                case 1:
                    resulta = suma(num1, num2)
                case 2:
                    resultado=resta(num1, num2 )             
                case 3:
                    resulta=multiplicacion(num1, num2  )
                case 4:
                    resultado=division(num1, num2  )      
                case 5:   
                    print("Saliendo de la calculadora. ¡Hasta luego!")
                    break   
                case _:
                    print("Opcion invalida. Por favor, seleccione una opcion valida (1-5)./n")
                    
        except ValueError:
            print("\nError: Debe ingresar un numero valido\n")
        except ZeroDivisionError:
            print("\nError: No se puede dividir por cero\n")
        else:
            print(f"El resultado es: {resultado}\n\n")
    print("Gracias por usar la calculadora.")
main()

print("Fin del programa")   