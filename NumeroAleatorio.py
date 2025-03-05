import random
numero_aleatorio = random.randint(1, 100)
adivinado = False

while not adivinado:
    intento = int(input("adivina el numero entre 1 y 100: "))

    if intento < numero_aleatorio:
        print("trata un numero más alto")

    elif intento > numero_aleatorio:
        print("trata un numero más bajo")

    else:
        print("ADIVINASTE!!")
        adivinado = True
  

