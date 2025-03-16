'''
Haz un programa que pida al usuario que ingrese una temperatura en
grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
mostrando el resultado.

'''

temp_celsius = float( input("Ingrese la temperatura en grados celsius"))      

temp_fahrenheit = ((temp_celsius*(9/5))+32)

print (f"{temp_celsius}°C = {temp_fahrenheit}°F")