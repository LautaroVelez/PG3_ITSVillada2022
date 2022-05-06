
try:
    n1=int(input("Ingrese numero 1"))
    n2=int(input("Ingrese numero 2"))
    print("la suma es", n1+n2)
    print("quiere seguir sumando?")
    sino=input()

    while sino=="s":
        n1=int(input("Ingrese numero 1"))
        n2=int(input("Ingrese numero 2"))
        print(n1+n2)
        print("quiere seguir sumando?")
        sino=input()
    else:
        print("Chau bro")
        
except:
    print("no se puede sumar letras con numeros")
