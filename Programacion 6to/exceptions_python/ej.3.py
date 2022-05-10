meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

try:
    input=int(input("Ingrese su numero de mes"))
    
    if input<13 and input>0:
        print("Su mes es:",meses[input-1])
    else:
        print("Introduce un numero valido wn")

except IndexError:
    print("Introduzca un numero valido")
except ValueError:
    print("Introduzca un numero wn")