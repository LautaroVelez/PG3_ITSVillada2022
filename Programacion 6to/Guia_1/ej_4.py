lista = []

def orden(lista):
    print("Escribi tu lista")
    lista = [int(item) for item in input().split()]
    lista.sort(reverse = True)
    print(lista)

orden(lista)