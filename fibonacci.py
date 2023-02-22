"""
* Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
* La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
* 0, 1, 1, 2, 3, 5, 8, 13...

"""

def fibonacci(n): # n es la posicion del numero en la secuencia
    a = 0
    b = 1
    for k in range(n):
        c = a + b
        a = b
        b = c
    return b


for x in range(50):
    print(fibonacci(x))