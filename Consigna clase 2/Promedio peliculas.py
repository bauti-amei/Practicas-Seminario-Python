
import funciones

movies_duration = []
funciones.cargar_lista(movies_duration)

prom = funciones.calcular_promedio(movies_duration)
if prom != -1:
    print(f"El promedio de duracion de las peliculas es {prom}")
    print(
        f"La cantidad de peliculas con duracion por el cima del promedio es {funciones.cant_superan_promedio(movies_duration)}")
