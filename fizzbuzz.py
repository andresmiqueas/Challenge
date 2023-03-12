"""
Reto #0: EL FAMOSO "FIZZ BUZZ”
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def my_fizzbuzz(): # DEFINO UNA FUNCION LLAMADA "my_fizzbuzz"
   for numero in range(1, 101): # ITERO "NUMERO" EN UN RANGO ENTRE 1 Y 100 (INCLUIDOS)
        if numero % 3 == 0 and numero % 5 == 0:
            print(numero, "fizzbuzz")
        elif numero % 3 == 0:
            print(numero, "fizz")
        elif numero % 5 == 0:
            print(numero, "buzz")  
        else:
            print(numero)


my_fizzbuzz()