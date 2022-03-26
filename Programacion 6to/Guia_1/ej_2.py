print("Ingrese su año:")
a = int(input())

def function(a):
    if a % 4 == 0 or a % 400 == 0 and a % 100 != 0:
        print("es bisiesto")
    else:
        print("no es bisiesto pa")

function(a)