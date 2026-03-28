numero = 690
while True:
    intento = int(input("Adivina el numero:"))
    if intento > 1000000:
        print("Mas bajo")
    elif intento < 500:
        print("Mas alto")
    elif intento == numero:
        print("Ganaste")
        break