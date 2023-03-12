"""
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""


def aragrama(string1, string2): # CREO UNA FUNCION LLAMADA "ANAGRAMA" QUE RECIBE COMO PARAMETRO DOS STRINGS
    if string1.lower() == string2.lower(): # SI SON DOS PALABRAS EXACTAMENTE IGUALES NO ES ANAGRAMA
        return False
    elif sorted (string1.lower()) == sorted(string2.lower()): # LLAMO A SORTED QUE ME ITERA CARACTER POR CARACTER Y LE DIGO QUE SI SON IGUALES PRINTEE VERDADERO
        print("True")
    else:
       print("False") # SI NO SON LOS MISMOS CARACTERES NO ES UN ANAGRAMA

aragrama("casa", "casa") #LLAMO A MI FUNCION Y LE PASO DOS STRINGS PARA COMPRARAR


def is_anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagrama("casa", "casa"))