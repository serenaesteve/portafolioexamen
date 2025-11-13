"""
Programa CRUD para la gestion del portafolio de piezas.

Este programa permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar)
sobre la base de datos 'portafolioexamen', que contiene las tablas 
'piezasportafolio' y 'categoriasportafolio'.

Refactorizado aplicando extraccion de funciones y documentacion mediante docstrings.
Autor: Serena Sania Esteve
Version: 2.0
"""

import mysql.connector


def conectar_bd():
    """
    Crea y devuelve una conexion y cursor a la base de datos 'portafolioexamen'.
    """
    conexion = mysql.connector.connect(
        host="localhost",
        user="serena",
        password="Examen123",
        database="portafolioexamen"
    )
    cursor = conexion.cursor()
    return conexion, cursor


def insertar_pieza(cursor, conexion):
    """
    Inserta una nueva pieza en la tabla 'piezasportafolio'.
    Pide al usuario los datos y los guarda en la base de datos.
    """
    titulo = input("Introduce el titulo de la pieza: ")
    descripcion = input("Introduce la descripcion de la pieza: ")
    fecha = input("Introduce la fecha de la pieza (YYYY-MM-DD): ")
    imagen = input("Introduce el nombre de la imagen: ")
    id_categoria = input("Introduce el id de la categoria: ")

    cursor.execute(
        "INSERT INTO piezasportafolio VALUES (NULL, %s, %s, %s, %s, %s)",
        (titulo, descripcion, fecha, id_categoria, imagen)
    )
    conexion.commit()
    print("Pieza insertada correctamente.")


def listar_piezas(cursor):
    """
    Muestra en pantalla todas las piezas del portafolio junto con su categoria.
    """
    cursor.execute("SELECT * FROM piezasportafolio;")
  
    lineas = cursor.fetchall()
    for linea in lineas:
        print(linea)


def actualizar_pieza(cursor, conexion):
    """
    Actualiza una pieza existente en la tabla 'piezasportafolio'.
    Pide el identificador y los nuevos datos al usuario.
    """
    identificador = input("Introduce el id de la pieza a actualizar: ")
    titulo = input("Introduce el nuevo titulo: ")
    descripcion = input("Introduce la nueva descripcion: ")
    fecha = input("Introduce la nueva fecha (YYYY-MM-DD): ")
    imagen = input("Introduce el nuevo nombre de la imagen: ")
    id_categoria = input("Introduce el nuevo id de la categoria: ")

    cursor.execute("""
        UPDATE piezasportafolio
        SET titulo = %s,
            descripcion = %s,
            fecha = %s,
            id_categoria = %s,
            imagen = %s
        WHERE Identificador = %s
    """, (titulo, descripcion, fecha, id_categoria, imagen, identificador))
    conexion.commit()
    print("Pieza actualizada correctamente.")


def eliminar_pieza(cursor, conexion):
    """
    Elimina una pieza de la tabla 'piezasportafolio' segun su identificador.
    """
    identificador = input("Introduce el id de la pieza a eliminar: ")
    cursor.execute("DELETE FROM piezasportafolio WHERE Identificador = %s", (identificador,))
    conexion.commit()
    print("Pieza eliminada correctamente.")


def mostrar_menu():
    """
    Muestra el menu principal con las opciones CRUD y devuelve la opcion elegida.
    """
    print("\n--- Gestion de portafolio v2.0 ---")
    print("1. Insertar pieza")
    print("2. Listar piezas")
    print("3. Actualizar pieza")
    print("4. Eliminar pieza")
    print("5. Salir")
    try:
        opcion = int(input("Escoge una opcion: "))
        return opcion
    except ValueError:
        print("Opcion no valida. Introduce un numero del 1 al 5.")
        return 0


def main():
    """
    Funcion principal del programa. Gestiona el flujo general y las llamadas a las funciones CRUD.
    """
    conexion, cursor = conectar_bd()

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            insertar_pieza(cursor, conexion)
        elif opcion == 2:
            listar_piezas(cursor)
        elif opcion == 3:
            actualizar_pieza(cursor, conexion)
        elif opcion == 4:
            eliminar_pieza(cursor, conexion)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion incorrecta. Intenta de nuevo.")

    cursor.close()
    conexion.close()


if __name__ == "__main__":
    main()
