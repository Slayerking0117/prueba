from registros import *

registro = []

while True:
    print("\n=== MENÚ ===")
    print("1. Registrar")
    print("2. Consultar lista")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        id = input("Id:  ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        programa = input("Programa:  ")
        estado = input("Estado: ")
        agregar_estudiante(registro, id , nombre, apellido, programa, estado)

    elif opcion == "2":
        mostrar_registro(registro)

    elif opcion == "3":
        nombre = input("Buscar: ")
        p = buscar_estudiante(registro, nombre)
        print(p if p else "No encontrado")

    elif opcion == "4":
        nombre = input("Producto: ")
        apellido = input("Nuevo precio: ")
        estado = input("Nueva cantidad: ")
        actualizar_informacion(registro, nombre, apellido, estado)

    elif opcion == "5":
        nombre = input("Eliminar: ")
        eliminar_estudiante(registro, nombre)
    
    elif opcion == "6":
        break

    else:
        print("Opción inválida")