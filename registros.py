

def agregar_estudiante(registro, id, nombre, apellido, estado, programa):
    """Agrega un estudiante al registro"""
    estudiante = {"Id": id,  "nombre": nombre, "apellido": apellido, "Programa": programa, "estado": estado}
    registro.append(estudiante)


def mostrar_registro(registro):
    """Muestra todos los estudiantes"""
    if not registro:
        print("Registro vacío")
        return

    for i in registro:
        print(f"{i['nombre']} | Apellido: {i['apellido']} | Estado: {i['estado']}")


def buscar_estudiante(registro, nombre):
    """Busca un estudiante por nombre"""
    for i in registro:
        if i["nombre"] == nombre:
            return i
    return None


def actualizar_informacion(registro, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza un producto"""
    p = buscar_estudiante(registro, nombre)
    if p:
        if nuevo_precio is not None:
            p["apellido"] = nuevo_precio
        if nueva_cantidad is not None:
            p["estado"] = nueva_cantidad
        return True
    return False


def eliminar_estudiante(registro, nombre):
    """Elimina un estudiante"""
    p = buscar_estudiante(registro, nombre)
    if p:
        registro.remove(p)
        return True
    return False

    