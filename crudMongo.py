import pymongo

def menu():
    print("Selecciona una operación:")
    print("1. Insertar alumnos")
    print("2. Actualizar direccion del alumno")
    print("3. Eliminar alumno")
    print("4. Mostrar todos los alumnos")
    print("0. Salir")

def insertar_documento(coleccion):
    nombre = input("Ingrese el nombre: ")
    rut = input("Ingrese el rut: ")
    edad = int(input("Ingrese la edad: "))
    direccion = input("Ingrese la direccion: ")
    documento = {"nombre": nombre, "rut": rut, "edad": edad, "direccion": direccion}
    coleccion.insert_one(documento)
    print("Documento insertado correctamente.")

def mostrar_documentos(coleccion):
    print("Documentos en la colección:")
    for doc in coleccion.find():
        print(doc)

def actualizar_documento(coleccion):
    rut = input("Ingrese el rut del alumno que desea actualizar: ")
    nueva_direccion = input("Ingrese la nueva direccion: ")
    # Buscar el documento por el nombre y actualizar la ciudad
    coleccion.update_one({"rut": rut}, {"$set": {"direccion": nueva_direccion}})
    print("Documento actualizado correctamente.")

def eliminar_documento(coleccion):
    rut = input("Ingrese el rut del alumno que desea eliminar: ")
    # Buscar y eliminar el documento por el RUT
    resultado = coleccion.delete_one({"rut": rut})
    if resultado.deleted_count > 0:
        print("Alumno eliminado correctamente.")
    else:
        print("No se encontró ningún alumno con ese RUT.")

def main():
    # Conectarse a MongoDB
    cliente = pymongo.MongoClient("localhost", 27017)

    # Crear una base de datos y una colección
    db = cliente["Guia01"]
    coleccion = db["lista_alumnos"]

    while True:
        menu()
        print("--------------------------------------------------------------------")
        opcion = int(input("Ingrese el número de la operación que desea realizar: "))
        if opcion == 1:
            insertar_documento(coleccion)
        elif opcion == 2:
            actualizar_documento(coleccion)
        elif opcion == 3:
            eliminar_documento(coleccion)
        elif opcion == 4:
            mostrar_documentos(coleccion)
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
