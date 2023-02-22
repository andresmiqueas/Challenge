"""
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""


def aragrama(string1, string2): # CREO UNA FUNCION LLAMADA "ANAGRAMA" QUE RECIBE COMO PARAMETRO DOS STRINGS
    if string1 == string2: # SI SON DOS PALABRAS EXACTAMENTE IGUALES NO ES ANAGRAMA
        print("Son dos palabras iguales")
    elif sorted (string1) == sorted(string2): # LLAMO A SORTED QUE ME ITERA CARACTER POR CARACTER Y LE DIGO QUE SI SON IGUALES PRINTEE VERDADERO
        print("verdadero")
    else:
       print("false") # SI NO SON LOS MISMOS CARACTERES NO ES UN ANAGRAMA


aragrama("papiro", "piparo") #LLAMO A MI FUNCION Y LE PASO DOS STRINGS PARA COMPRARAR
