"""
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""


def anagrama(string1, string2):
    if string1 == string2:
        print("SON IGUALES")
    elif sorted(string1) == sorted(string2):
        print("true")
    else:
       print("false")


anagrama("hola","hola")