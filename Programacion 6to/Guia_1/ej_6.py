print("Escribi tu palabra")
cadena=input()

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

contar_vocales(cadena)