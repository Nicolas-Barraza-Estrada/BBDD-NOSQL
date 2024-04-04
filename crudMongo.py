import pymongo
import pprint
def menu():
    print("Selecciona una operación:")
    print("1. Insertar alumnos")
    print("2. Actualizar direccion del alumno")
    print("3. Eliminar alumno")
    print("4. Mostrar todos los alumnos")
    print("5. Mostrar solo los alumnos de Concepción")
    print("6. Mostrar solo los alumnos de Talcahuano")
    print("7. Mostrar solo los alumnos de San Pedro de la Paz")
    print("0. Salir")

def insertar_base(coleccion):
    coleccion_base = []
    #ciudades: Concepción, Talcahuano, San Pedro de la Paz, Chiguayante, Hualpén, Hualqui, Tomé, Penco, Lota, Coronel, Florida, Santa Juana
    coleccion_base.append({"nombre": "Juan", "rut": "12345678-9", "edad": 20, "direccion": "Calle 1", "ciudad": "Concepción"})
    coleccion_base.append({"nombre": "Pedro", "rut": "23456789-0", "edad": 21, "direccion": "Calle 2", "ciudad": "Talcahuano"})
    coleccion_base.append({"nombre": "Diego", "rut": "34567890-1", "edad": 22, "direccion": "Calle 3", "ciudad": "San Pedro de la Paz"})
    coleccion_base.append({"nombre": "Jose", "rut": "45678901-2", "edad": 23, "direccion": "Calle 4", "ciudad": "Concepción"})
    coleccion_base.append({"nombre": "Carlos", "rut": "56789012-3", "edad": 24, "direccion": "Calle 5", "ciudad": "Talcahuano"})
    coleccion_base.append({"nombre": "Mario", "rut": "67890123-4", "edad": 25, "direccion": "Calle 6", "ciudad": "San Pedro de la Paz"})
    coleccion_base.append({"nombre": "Luis", "rut": "78901234-5", "edad": 26, "direccion": "Calle 7", "ciudad": "Concepción"})
    coleccion_base.append({"nombre": "Jorge", "rut": "89012345-6", "edad": 27, "direccion": "Calle 8", "ciudad": "Talcahuano"})
    coleccion_base.append({"nombre": "Felipe", "rut": "90123456-7", "edad": 28, "direccion": "Calle 9", "ciudad": "San Pedro de la Paz"})
    coleccion_base.append({"nombre": "Andres", "rut": "81234567-8", "edad": 29, "direccion": "Calle 10", "ciudad": "Chiguayante"})
    coleccion_base.append({"nombre": "Cristian", "rut": "72345678-9", "edad": 30, "direccion": "Calle 11", "ciudad": "Talcahuano"})
    coleccion_base.append({"nombre": "Javier", "rut": "63456789-0", "edad": 31, "direccion": "Calle 12", "ciudad": "Hualpén"})
    coleccion_base.append({"nombre": "Gabriel", "rut": "54567890-1", "edad": 32, "direccion": "Calle 13", "ciudad": "Hualqui"})
    #Llena la base de datos con adtos de prueba
    for documento in coleccion_base:
        coleccion.insert_one(documento)
    print("Se han insertado los documentos de prueba.")
    return


def insertar_documento(coleccion):
    try:
        nombre = input("Ingrese el nombre: ")
        rut = input("Ingrese el rut: ")
        edad = int(input("Ingrese la edad: "))
        direccion = input("Ingrese la direccion: ")
        Ciudad = input("Ingrese la ciudad: ")
        documento = {"nombre": nombre, "rut": rut, "edad": edad, "direccion": direccion, "ciudad": Ciudad}
        #reviar el rut
        if coleccion.find_one({"rut": rut}):
            print("El rut ya existe en la base de datos")
        else:
        # Insertar un documento en la colección
            coleccion.insert_one(documento)
            print("Se ha insertado: ")
            print(coleccion.find_one({"rut": rut}))
        print("--------------------------------------------------------------------")
    except Exception as e:
        print("Error:", e)
        print("--------------------------------------------------------------------")

def actualizar_documento(coleccion):
    rut = input("Ingrese el rut del alumno que desea actualizar: ")
    #comprobar si el rut existe
    if not coleccion.find_one({"rut": rut}): 
        print("No se encontró ningún alumno con ese RUT.")
        print("--------------------------------------------------------------------")
        return
    nueva_direccion = input("Ingrese la nueva direccion: ")
    nueva_ciudad = input("Ingrese la nueva ciudad: ")
    # Buscar el documento por el nombre y actualizar la direccion y ciudad
    resultado = coleccion.update_one({"rut": rut}, {"$set": {"direccion": nueva_direccion, "ciudad": nueva_ciudad}})
    if resultado.modified_count > 0:
        print("Alumno actualizado correctamente.")
    else:
        print("No se encontró ningún alumno con ese RUT.")
    print("--------------------------------------------------------------------")
    

def mostrar_documentos(coleccion):
    print("Documentos en la colección:")
    try:
        for documento in coleccion.find():
            print(documento)
    except Exception as e:
        print("Error:", e)
    print("--------------------------------------------------------------------")

def mostrar_documentos_por_ciudad(coleccion, ciudad):
    print("Documentos en la colección:")
    try:
        for documento in coleccion.find({"ciudad": ciudad}):
            print(documento)
    except Exception as e:
        print("Error:", e)
    print("--------------------------------------------------------------------")


def eliminar_documento(coleccion):
    rut = input("Ingrese el rut del alumno que desea eliminar: ")
    # Buscar y eliminar el documento por el RUT
    resultado = coleccion.delete_one({"rut": rut})
    if resultado.deleted_count > 0:
        print("Alumno eliminado correctamente.")
    else:
        print("No se encontró ningún alumno con ese RUT.")
    print("--------------------------------------------------------------------")


def main():
    # Conectarse a MongoDB
    cliente = pymongo.MongoClient("localhost", 28017) # cambiar la direccion del localhost a 27017

    # Crear una base de datos y una colección
    db = cliente["Guia01"]
    coleccion = db["lista_alumnos"]

    # Insertar documentos de prueba si la base de datos esta vacia
    if coleccion.count_documents({}) == 0:
        insertar_base(coleccion)
    mostrar_documentos(coleccion)
    while True:
        menu()
        opcion = int(input("Ingrese el número de la operación que desea realizar: "))
        if opcion == 1:
            insertar_documento(coleccion)
        elif opcion == 2:
            actualizar_documento(coleccion)
        elif opcion == 3:
            eliminar_documento(coleccion)
        elif opcion == 4:
            mostrar_documentos(coleccion)
        elif opcion == 5:
            mostrar_documentos_por_ciudad(coleccion, "Concepción")
        elif opcion == 6:
            mostrar_documentos_por_ciudad(coleccion, "Talcahuano")
        elif opcion == 7:
            mostrar_documentos_por_ciudad(coleccion, "San Pedro de la Paz")
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
