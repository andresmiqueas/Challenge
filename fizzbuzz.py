"""
* Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

def my_fizzbuzz(): # DEFINO UNA FUNCION LLAMADA "my_fizzbuzz"
   for numero in range(1, 100): # ITERO "NUMERO" EN UN RANGO ENTRE 1 Y 100 (INCLUIDOS)
    if(numero % 3 == 0): #SI EL RESTO DE DIVIDIR "NUMERO" POR 3 DA 0
        print("fizz")
    elif(numero % 5 == 0): #SI EL RESTO DE DIVIDIR "NUMERO" POR 5 DA 0
        print("buzz")
    elif (numero % 3 == 0 and numero % 5 == 0): #SI EL RESTO DE DIVIDIR "NUMERO" POR 3 Y POOR 5 DA 0
        print("fizzbuzz")
    else:
        ("Salir")



my_fizzbuzz()

