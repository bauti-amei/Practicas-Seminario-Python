'''
Desarrolla un programa que solicite al usuario que ingrese su edad y luego
calcule y muestre cuántos años le faltan para alcanzar los 100 años.

'''

edad = int( input ("Ingrese su edad"))

if (edad < 0):
    print ("Edad incorrecta")
elif (edad < 100):
    print (f"A usted le faltan {100-edad} años para llegar a los 100")
elif (edad == 100):
    print ("Usted ya llego a los 100 años")
else:
    print ("Usted tiene mas de 100 años")
