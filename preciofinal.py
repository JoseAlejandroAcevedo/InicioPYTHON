
print("Bienvenido, vamos a comprar, dinos el precio, ganancia e impuesto")

precio = input("ingrese el preio: ")
precio = float(precio)

ganancia = input("ingrese la ganancia: ")
ganancia = float(ganancia)

impuesto = input("ingrese el impuesto: ")
impuesto = float(impuesto)

def CalcularImpuesto(impuesto, precio):
    return impuesto * precio

def CalcularGanancia(ganancia, precio):
    return ganancia * precio

def CalcularPrecioFinal(precio, impuesto, ganancia):
    precio1 = CalcularGanancia(ganancia, precio) + precio
    impuestoVenta = CalcularImpuesto(impuesto, precio)
    return precio1 + impuestoVenta

print(CalcularPrecioFinal(precio, impuesto, ganancia))




