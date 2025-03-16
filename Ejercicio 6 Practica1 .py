
'''
Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
listas, una con los número pares y otras con los que son impares. Imprima
las listas al terminar de procesarlas.
'''

lista = range (11)

lista_par = [n for n in lista if n%2==0]
lista_impar = [n for n in lista if n%2!=0]
  
print ("Lista nueros pares ", lista_par)
print ("Lista numeros impares ",lista_impar)