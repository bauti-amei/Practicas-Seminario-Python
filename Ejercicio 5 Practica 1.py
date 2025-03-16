'''
Implementa un programa que solicite al usuario que ingrese una lista de
números. Luego, imprime la lista pero detén la impresión si encuentras un
número negativo. Nota: utilice la sentencia break cuando haga falta.
'''

lista_numeros = []

cant_elementos = int(input ("Ingrese la cantidad de numeros que trendra la lista"))

for i in range(cant_elementos):
    nuevo_num = int (input ("Ingrese un numero"))
    lista_numeros.append(nuevo_num)

print ("La lista de numeros es : ", end=" ")

for i in range (cant_elementos):
    if lista_numeros [i] < 0 :
        print (" SE ENCONTRO UN NEGATIVO")
        break
    else:
        print (lista_numeros[i], end=" - ")

