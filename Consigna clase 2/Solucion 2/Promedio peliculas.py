
import funciones


# Cargo lista por teclado con las duraciones de las peliculas
movies_duration = []
funciones.cargar_lista(movies_duration)

# Calculo el promedio
prom = funciones.calcular_promedio(movies_duration)
# Si la funcion retorna -1, la lista esta vacia
if prom != -1:
    print(f"El promedio de duracion de las peliculas es {prom}")
    print(
        f"La cantidad de peliculas con duracion por el cima del promedio es {funciones.cant_superan_promedio(movies_duration)}")

