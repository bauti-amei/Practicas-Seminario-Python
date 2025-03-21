
def cargar_lista(movies_duration):
    '''Recibe una lista por parametro y carga los valores ingresados por teclado'''
    minutes = int(
        input("Ingresá la duración de una película (0 para finalizar): "))
    while minutes != 0:
        movies_duration.append(minutes)
        minutes = int(
            input("Ingresá la duración de una película (0 para finalizar): "))


def calcular_promedio(movies_duration):
    '''Recibe una lista por parametro y devuelve el promedio de los elementos/-1 si la lista esta vacia'''
    if len(movies_duration) != 0:
        return (sum(movies_duration)/len(movies_duration))
    else:
        print("La lista esta vacia")
        return -1


def cant_superan_promedio(movies_duration):
    '''Recibe una lista por parametro y devuelve la cantidad de elementos que superan el promedio'''
    cant = 0
    prom = calcular_promedio(movies_duration)
    for time in movies_duration:
        if time > prom:
            cant += 1
    return cant


# Cargo lista por teclado con las duraciones de las peliculas
movies_duration = []
cargar_lista(movies_duration)

# Calculo el promedio
prom = calcular_promedio(movies_duration)
# Si la funcion retorna -1, la lista esta vacia
if prom != -1:
    print(f"El promedio de duracion de las peliculas es {prom}")
    print(
        f"La cantidad de peliculas con duracion por el cima del promedio es {cant_superan_promedio(movies_duration)}")
