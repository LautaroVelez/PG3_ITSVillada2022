num1=int(input("Ingrese el numero 1"))
num2=int(input("Ingrese el numero 2"))

try:
    div=(num1/num2)
    print("El resultado de su division es: ",div)
except ZeroDivisionError:
    print("No se puede dividir por cero bro")
except ValueError:
    print("Valor invalido bro")
