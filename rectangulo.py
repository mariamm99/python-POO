# -*- coding: utf-8 -*-

class Rectangulo:
    """
    Versión 1.0
    
    Esta clase representa objetos de tipo rectángulo.

    Acciones: cálculo del perímetro, área, dibujar y comparar.

    Hay cosas que mejorar, en la siguiente se explica
    """
    def __init__(self, base, altura):
        """
        Constructor de la clase
        :param base: base del rectángulo
        :param altura: altura del rectángulo
        """
        self.base = base
        self.altura = altura
    
    def perimetro(self):
        """
        Devuelve el perímetro del rectángulo
        :return perímetro del rectángulo
        """
        return 2 * (self.base + self.altura)
    
    def area(self):
        """
        Devuelve el área del rectángulo
        :return área del rectángulo
        """
        return self.base * self.altura
    
    def compara(self, rectangulo):
        """
        Compara nuestro rectángulo con otro
        :param rectangulo: objeto con el que comparamos el actual
        :return >0 si mayor, 0 si igual, <0 si menor
        """
        return self.area() - rectangulo.area()
    
    def es_gemelo(self, rectangulo):
        """
        Comprueba si el objeto pasado es el mismo rectángulo o sea,
        tiene la misma base y altura
        :param rectangulo: objeto con el que comparamos el actual
        :return True o False
        """
        return self.base == rectangulo.base and self.altura == rectangulo.altura

    def muestra(self):
        """
        Muestra en pantalla el rectángulo
        """
        for i in range(self.altura):
            print("*" * self.base)

if __name__ == "__main__":

    r1 = Rectangulo(4, 1)
    r2 = Rectangulo(3, 2)
    print(f"Probamos clase Rectángulo con ({r1.base},{r1.altura}) y ({r2.base},{r2.altura})\n")

    # Mostramos los rectángulos
    r1.muestra()
    print()
    r2.muestra()

    # Comparamos los rectángulos
    print("Resultado de comparar r1 con r2:", r1.compara(r2))
    print("¿Son gemelos?", r1.es_gemelo(r2))

    # Magnitudes de los rectángulos
    print("Área r1:", r1.area(), "Perímetro r1:", r1.perimetro())
    print("Área r2:", r2.area(), "Perímetro r2:", r2.perimetro())