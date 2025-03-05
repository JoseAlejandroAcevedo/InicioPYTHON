def comparar_cadenas():
    cadena1 = input("ingrese la primera cadenaa: ")
    cadena2 = input("ingrese la segunda cadena: ")

    if cadena1 == cadena2:
        print("las cadenas son iguales")
    else:
        print("las cadenas son diferentes")

        if cadena1 > cadena2:
            print(f"{cadena1} es mayor que {cadena2}")
        else:
            print(f"{cadena1} es menor que {cadena2}")

comparar_cadenas()