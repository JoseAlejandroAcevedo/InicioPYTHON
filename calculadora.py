def calculadora():
    print("calculadora basica")
    print("seleccione una operacion")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")

    opcion = input("ingrese un numero: ")

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        if opcion == "1":
            print(f"resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == "2":
            print(f"resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == "3":
            print(f"resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print(f"Error: no se puede dividir por cero")
    else:
        print("Error: opcion invalida")  

calculadora()  