"""
@author Maria

version 2.0

Atributos: base y altura
Acciones: perímetro, area, madificador atributo(set), observador(get), comparar y dibujar
"""



class Rectangulo:
    """
    Esta clase representa objetos de tipo rectangulo.
    """
    def __init__(self, base, altura):
        """
        Costructor de la clase
        :param base: base del rectangulo
        :param altura: altura del rectangulo
        """
        self.__base = base
        self.__altura = altura

    def perimetro(self):
        """
        :return: perimetro del rectangulo
        """

        return 2*(self.__base + self.__altura)

    def area(self):
        """
        :return: area del rectángulo
        """
        return self.__base * self.__altura

    def compara(self, otro):
        """
        Compara nuestro rectangulo con otro
        :param otro: objeto con el que comparamos el actual
        :return: >0 si es mayor, 0 si es igual y <0 si es menor.
        """
        return self.area()-otro.area()

    def esgemelo(self, otro):
        """
        comprueba si el objeto pasado es el mismo rectángulo, tiene igual base y altura
        :return: True o False
        """
        return self.__base == otro.base and self.__altura == otro.altura

    def muestra(self):
        """
        Muestra en pantalla el rectángulo
        :return:
        """
        for i in range(self.__altura):
            print("*" * self.__base)

if __name__== "__main__":
    r1= Rectangulo(4, 1)
    r2= Rectangulo(3, 2)

    r1.muestra()
    r2.muestra()

    print("comparar r1 con r2", r1.compara(r2))

    print("r1 son gemelos", r1.esgemelo(r2))

    print("area r1:", r1.area(), "perimetro r1:" , r1.perimetro() )
    print("area r2:", r2.area(), "perimetro r2:" , r2.perimetro() )