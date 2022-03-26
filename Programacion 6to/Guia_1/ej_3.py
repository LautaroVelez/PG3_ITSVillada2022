print("Escribi el ancho")
ancho = int(input())

print("Escribi el alto")
alto = int(input())

print("Escribi el caracter")
caracter = str(input())

def imprimir(ancho,alto,caracter):
    for i in range (0,alto):
        print(caracter*ancho)


imprimir(ancho,alto,caracter)