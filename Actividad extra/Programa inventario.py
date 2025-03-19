import funcionalidades
import sys


# El inventario sera un diccionario donde la clave es el nombre del producto y el valor la cantidad
inventario = {}

# Imprimo el menu de opciones
funcionalidades.imprimir_menu()

# El usuario seleccionara una opcion
opcion = int(input("Seleccione una opcion :"))
while opcion != 4:
    if (opcion == 1):
        funcionalidades.agregar_producto(inventario)
    elif (opcion == 2):
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar")
        funcionalidades.eliminar_producto(inventario, nombre_eliminar)
    elif (opcion == 3):
        funcionalidades.mostrar_inventario(inventario)
    elif (opcion == 4):
        sys.exit
    else:
        print("La opcion ingresada no es valida")
    funcionalidades.imprimir_menu()
    opcion = int(input("Seleccione una opcion :"))
    
