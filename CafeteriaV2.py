total = 0
total1 = 0
total2 = 0
total3 = 0  
total_general = 0
while True:
    print("Registro de producto:\n cafe = 4000\n capuchino = 7000\n pastel = 6000\n salir. ")
    venta = input().lower()
    if venta == "cafe":
        total1 += 4000
        total_general += total1
    elif venta == "capuchino":
        total2 += 7000
        total_general += total2
    elif venta == "pastel":
        total3 += 6000
        total_general += total3
    elif venta == "salir":
        
        break
if total_general > 20000:
    descuento = total_general * 0.10
    total = total_general - descuento
    print(f"total es: {total}")
else:
    print(f"total es: {total_general}")
        
    
        
    
            
    