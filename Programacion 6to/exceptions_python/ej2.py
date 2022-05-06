
try:
    n1=int(input("Ingrese numero 1"))
    n2=int(input("Ingrese numero 2"))
    print("la division es", n1/n2)

except ZeroDivisionError:
    print("no se puede dividir por cero")
