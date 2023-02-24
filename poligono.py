"""
* Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
* La función recibirá por parámetro sólo UN polígono a la vez.
* Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* Imprime el cálculo del área de un polígono de cada tipo.
"""


opcion = int(input("Ingrese 1 para calcular el area de un Triángulo, 2 para un Cuadrado o 3 para un Rectángulo "))

def poligono():
    if opcion == 1:
        print("Triangulo")
        lado = int(input("Ingrese lado: "))
        base= int(input("Ingrese base: "))
        print(f"El area de un Triangulo es {(base * lado) / 2} metros cuadrados")
    elif opcion == 2:
        print("Cuadrado")
        lado = int(input("Ingrese lado: "))
        print(f"El area de un Cuadrado es {lado ** 2} metros cuadrados")
    elif opcion == 3:
        print("Rectángulo")
        lado = int(input("Ingrese lado: "))
        base = int(input("Ingrese base: "))
        print(f"El area de un Rectángulo es {(base * lado)} metros cuadrados")
    else:
        print("Error")




poligono()