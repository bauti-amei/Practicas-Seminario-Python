'''
Cree un programa que dada una lista de números imprima sólo los que son
pares. Nota: utilice la sentencia continue donde haga falta.

'''

lista_numeros = range (10)      

for i in lista_numeros:
    if ((lista_numeros[i] % 2) != 0):
        continue
    print (lista_numeros[i], end="-")
        