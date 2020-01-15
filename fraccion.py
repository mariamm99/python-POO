

class Fraccion:
    """
    Contruir un objeto Fraccion pasándole el numerador y el denominador.
    Obtener la fracción como cadena de caracteres.
    Obtener y modificar numerador y denominador. No se puede dividir por cero.
    Obtener resultado de la fracción (número real).
    Multiplicar la fracción por un número.
    Multiplicar, sumar y restar fracciones.
    Simplificar la fracción.
    """

    __numerador = 1
    __denominador = 1

    def __init__(self, numerador, denominador):
        """
        Constructor de la clase
        :param numerador: numerador del rectángulo
        :param denominador: denominador del rectángulo
        """
        self.set_numerador(numerador)
        self.set_denominador(denominador)

    @property
    def numerador(self):
        return self.__numerador

    #@numerador.setter
    def set_numerador(self, numerador):
       self.__numerador = numerador

    @property
    def denominador(self):
        return self.__denominador

    #@denominador.setter
    def set_denominador(self, value):
        correcto = self.es_correcto(value)
        if correcto:
            self.__denominador = value
        else:
            # Mucho mejor sería lanzar una excepción
            print("ERROR. denominador = 0")

    @staticmethod
    def es_correcto(value):
        return type(value) == type(1.0) and value != 0

    def cadenaCaracteres(self):
        """
        devuelve cadena de caracteres
        :return: francción en cadena de caracteres
        """
        print(self.__numerador, " / ", self.__denominador)

    def resultado(self):
        """
        Devuelve el perímetro del rectángulo
        :return perímetro del rectángulo
        """
        return self.__numerador / self.__denominador

    def multiplicacion(self, nMultiplicar):
        """
        Mulitiplica la fracción por un numero
        :return:
        """
        return self.__numerador * nMultiplicar / self.__denominador

    def multiplicarFraccion(self, otra):
        """
        multiplicar dos fracciones
        :return:
        """
        resultadoNum= self.__numerador * otra.__numerador
        resultadoDen= self.__denominador * otra.__denominador
        return str(resultadoNum) + "/" + str(resultadoDen)


    def sumaFraccion(self, otra):
        """
        multiplicar dos fracciones
        :return:
        """
        return self.__numerador / self.__denominador + otra.__numerador / otra.__denominador

    def restaFraccion(self, otra):
        """
        multiplicar dos fracciones
        :return:
        """
        return self.__numerador / self.__denominador - otra.__numerador / otra.__denominador

    def simplificar(self):
        """
        simplificar fracción
        el usuario dice por cuanto simplificar? tengo q decirlo yo?

        :return:
        """
        mcm=0
        for i in range(10, 1, -1):
            if self.__numerador%i==0 and self.__denominador%i==0:
                mcm=i
                self.__numerador= self.__numerador / i
                self.__denominador= self.__denominador / i
                print("mcm = ", i)
        return Fraccion(self.__numerador, self.__denominador)


if __name__ == "__main__":
    f1 = Fraccion(6.0, 2.0)
    f2 = Fraccion(60.0, 40.0)
    print(f"Probamos clase Rectángulo con ({f1.numerador},{f1.denominador}) y ({f2.numerador},{f2.denominador})\n")
    f1.cadenaCaracteres()
    f2.cadenaCaracteres()

    # Resultado
    print("Resultado de  r1:", f1.resultado())
    print("Resultado de r2", f2.resultado())

    # multiplicar por número
    nMultiplicar = int(input("Indique por cuanto quiere multiplicar la fracción"))
    print(f1.multiplicacion(nMultiplicar))

    # multiplicar fracción
    print("el resultado de multiplicar las dos fracciones", f1.multiplicarFraccion(f2))

    # suma fracción
    print("el resultado de sumar las dos fracciones", f1.sumaFraccion(f2))

    # resta fracción
    print("el resultado de restar las dos fracciones", f1.restaFraccion(f2))

    # simplificar fracción
    f3=f2.simplificar()

    print("simplificar fracción entre resultado: ", f3.numerador, "/", f3.denominador)

    #comprobar fracciones correcta
    f3 = Fraccion(6.0, 0)
    f3.simplificar()

