print("Escribi tu palabra")
cadena=input()

def contar_vocales(string):
	contador = 0
	for letra in string:
		if letra in "aeiou":
			contador += 1
	return print("En tu frase hay ",contador, " vocales")

contar_vocales(cadena)