import random
import string
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

puntaje = 0

# Creo una lista con 3 preguntas al azar con sus respectivas opciones y su respuesta correcta
questions_to_ask = random.sample(
    list(zip(questions, answers, correct_answers_index)), k=3)
for preguntas, opciones, respuesta in questions_to_ask:
    # Muestro la pregunta con sus opciones
    print(preguntas)
    for i, opcion in enumerate(opciones):
        print(i+1, ".", opcion)

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta : ")
        # Se verifica si la respuesta ingresada es un int y si esta dentro del rango valido
        if not (user_answer in string.digits and ((int(user_answer) in range(5)) == True)):
            print("Respuesta no valida")
            sys.exit(1)
        # Se convierte la respuesta del usuario en el formato correcto
        user_answer = int(user_answer)-1
        # Se verifica si la respuesta es correcta
        if user_answer == respuesta:
            print("¡Correcto!")
            puntaje += 1
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(opciones[respuesta])
        puntaje -= 0.5

    # Se imprime un blanco al final de la pregunta
    print()

# Imprimo el puntaje, considerando cero como el puntaje mas bajo
if puntaje < 0:
    puntaje = 0
print("Usted obtuvo un puntaje de : ", puntaje)
