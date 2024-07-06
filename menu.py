import os
import globales
import productos
import estadisticas
os.system("cls")

def menu_estadisticas():
    while True:
        os.system("cls")
        print("=== ESTADISTICAS ====")
        print("1. Producto con valor más alto.")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos")
        print("5. Salir")

        opciones = globales.seleccionar_opcion(5)

        if opciones == 1:
            estadisticas.valor_mas_alto()
        elif opciones == 2:
            estadisticas.valor_mas_bajo()
        elif opciones == 3:
            estadisticas.promedio()
        elif opciones == 4:
            estadisticas.media_geometrica()
        elif opciones == 5:
            print("5. Salir.")
            return

        input("")

def menu_general():
    while True:
        os.system("cls")
        print("=== MENU ====")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")

        opciones = globales.seleccionar_opcion(3)

        if opciones == 1:
            productos.asignar_montos()
        elif opciones == 2:
            menu_estadisticas()
        elif opciones == 3:
            print("3. Salir del programa.")
            print("Desarrollado por Ernesto")
            return

        input("")


menu_general()