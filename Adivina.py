numero = 69
while True:
    intento = int(input("Adivina el numero:"))
    if intento < 100 and intento > 49:
        print("Mas bajo")
    elif intento < 50:
        print("Mas alto")
    elif intento == numero:
        print("Ganaste")
        break