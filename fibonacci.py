"""
* Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
* La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
* 0, 1, 1, 2, 3, 5, 8, 13...


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

"""

def fibonacci(): 

    n1 = 0 #PARA EMPEZAR TENGO QUE SUMAR 1 Y 0
    n2 = 1

    for index in range(1, 51): #HAGO UN BUCLE DE INDEX ENTRE 1 Y 51 (SACO LOS PRIMEROS 50)
 
        print(n1) #PRINTEO LOS NUMEROS EMPEZANDO DESDE EL 0
        n3 = n1 + n2 #CREO N3 QUE ES EL RESULTADO DE LA SUMA DE 0 + 1 
        n1 = n2 #ASIGO EL NUEVO VALOR A N1
        n2 = n3 #ASIGO EL NUEVO VALOR A N2

fibonacci()

