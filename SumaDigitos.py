numero = input("ingrese un numero: ")
suma = 0

for digito in numero:
    suma += int(digito)

print(f"La suma de los digitos de {numero} es {suma}")