'''
Escribe un programa que tome una lista de números enteros como entrada
del usuario. Luego, convierte cada número de la lista a string y únelos en
una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
número que sea múltiplo de 3 de la cadena final.
'''

lista_numeros = []
lista_str = ""

cant_elementos = int(input("Ingrese la cantidad de elementos de la lista"))

for i in range(cant_elementos):
    lista_numeros.append(int(input("Ingrese un numero")))

for i in range(cant_elementos):
    if lista_numeros[i] % 3 != 0:
        lista_str = lista_str + str(lista_numeros[i]) + "-"

print(f"La lista de numeros convertidos a char, sin los multiplos de 3 es : {lista_str}")
