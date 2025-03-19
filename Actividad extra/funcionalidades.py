
def imprimir_menu ():
    print("--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    print ()

def agregar_producto(inventario):
    '''Agrega un nuevo producto al inventario en caso que este no exista y que la cantidad sea un nro valido'''
    print("--- Nuevo producto ---")
    nombre_producto_nuevo = input("Ingrese el nombre del nuevo producto")
    # Verifico que el producto no exista en inventario
    if nombre_producto_nuevo in inventario:
        print("El producto ya fue ingresado")
    else:
        cantidad_producto_nuevo = int (input("Ingrese la cantidad del producto nuevo"))
        # Verifico que la cantidad se un nro valido
        if cantidad_producto_nuevo <= 0:
            print("La cantidad ingresada en incorrecta")
        # Agrego el producto al inventario
        else:
            inventario[nombre_producto_nuevo] = cantidad_producto_nuevo
            print(f"El producto {nombre_producto_nuevo} con cantidad {cantidad_producto_nuevo} unidades, fue agregado al inventario")
    print ()


def eliminar_producto(inventario, nombre_eliminar):
    ''' Recibe como parametro el nombre de un producto y en caso que se encuentre en el inventario lo elimina'''
    if not (nombre_eliminar in inventario):
        print(
            f"El producto de nombre {nombre_eliminar} no se encuentra en el inventario")
    else:
        # Elimino producto del inventario
        del (inventario[nombre_eliminar])
        print(f"Se ha eliminado el producto {nombre_eliminar} del inventario")
    print ()


def mostrar_inventario(inventario):
    '''Recorro e imprimo todos los productos del inventario'''
    if (len (inventario) == 0):
        print("El inventario esta vacio")
    else:
        print("--- Inventario actual ---")
        for nombreProducto, cantidad in inventario.items():
            print(f"Producto: {nombreProducto} - Cantidad : {cantidad}")
    print ()
