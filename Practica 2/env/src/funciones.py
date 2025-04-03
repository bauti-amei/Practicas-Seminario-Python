puntuacion = {'kills' : 3, 'assists' : 1, 'deaths': -1}

def calcular_puntaje (resultados_jugador):
    puntaje = 0
    for accion in puntuacion:
        puntaje = puntaje + resultados_jugador[accion]*puntuacion[accion]
    return puntaje

def calcular_MVP(resultados_ronda):
    '''Recibe los resultados de una ronda y retorna el nombre del jugador que fue el mejor jugador de la ronda'''
    puntos_max = -1
    for jugador in resultados_ronda:
        if calcular_puntaje(resultados_ronda[jugador])>puntos_max:
            puntos_max = calcular_puntaje (resultados_ronda[jugador])
            nombre_mejor_jugador = jugador
    return nombre_mejor_jugador

def imprimir_ordenado (resultados_ronda):
    for jugador, resultados in sorted(resultados_ronda.items(), key = lambda item: item[1]['puntos'], reverse=True):
        player = f'Jugador : {jugador}'
        for accion in resultados:
            player += f' -  {accion} : {resultados_ronda[jugador][accion]}'
        print (player)

        