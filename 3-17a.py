palabras = {}
texto = input("Introduce un texto: ")
palabra = ""

for i in range(0, len(texto)):
	if texto[i] != " ":
		palabra += texto[i]

	if texto[i] == " " or i == len(texto)-1:
		palabras[palabra] = 0
		print(palabra)
		palabra = ""

for i in range(0, len(texto)):
	if texto[i] != " ":
		palabra += texto[i]

	if texto[i] == " " or i == len(texto)-1:
		palabras[palabra] += 1
		palabra = ""
