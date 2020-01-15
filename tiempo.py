class Tiempo:
    """
      Versión 1.0

    Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:
        t = Tiempo(1, 20, 30)
    donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.

     Sumar y restar otro objeto de la clase Tiempo.
    Sumar y restar segundos, minutos y/o horas.
    Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
    Realiza un programa de prueba para comprobar que la clase funciona bien.
    """

    __horas    = 0
    __minutos  = 0
    __segundos = 0

    def __init__(self, horas, minutos, segundos):
        """
        Constructor de la clase
        :param hora:
        :param minutos:
        :param segundos:
        """
        self.__horas = horas
        self.set_minutos(minutos)
        self.set_segundos(segundos)

    def valorCorrecto(self, value):
        """
        :return: true o false
        """
        return type(value) == type(1) and 0 < value < 60

    @property
    def horas(self):
        """
        :return: horas
        """
        return self.__horas

    def set_horas(self, horas):
        self.__horas = horas


    @property
    def minutos(self):
        return self.__minutos

    #@minutos.setter
    def set_minutos(self, value):
        if self.valorCorrecto(value):
            self.__minutos = value
        else:
            print("ERROR: datos erroneos")

    @property
    def segundos(self):
        return self.__segundos

    #@segundos.setter
    def set_segundos(self, value):
        if self.valorCorrecto(value):
            self.__segundos = value
        else:
            print("ERROR: datos erroneos")

    def toSegundos(self):
        """
        pasar a segundos
        :return: segundos
        """
        segundos=self.__horas*3600+self.__minutos*60+self.__segundos
        return segundos

    def toHoras(self, segundos):
        """
        pasar segundos a hh, mm, ss
        :param segundos:
        :return:
        """
        return Tiempo(int(segundos/3600), int((segundos/60)%60), segundos%60)


    def suma(self, t2):
        """
        Devuelve el tiempo sumado en xh xm xs
        :return suma de tiempo
        """
        segundos=self.toSegundos()+t2.toSegundos()
        resultado=self.toHoras(segundos)

        return resultado

    def resta(self, t2):
        """
        Devuelve el tiempo restado en xh xm xs
        :return suma de tiempo
        """
        segundos = self.toSegundos() - t2.toSegundos()
        resultado = self.toHoras(segundos)

        return resultado

    def sumaHora(self, h):
        """
        Devuelve el tiempo sumado en xh xm xs
        :return suma de horas
        """

        return Tiempo(self.horas+h, self.minutos, self.segundos)

    def sumaMinutos(self, m):
        """
        Devuelve el tiempo sumado en xh xm xs
        :return suma de horas
        """
        segundos = self.toSegundos() + m*60
        resultado = self.toHoras(segundos)

        return resultado

    def sumaSegundos(self, s):
        """
        Devuelve el tiempo sumado en xh xm xs
        :return suma de horas
        """
        segundos = self.toSegundos() + s
        resultado = self.toHoras(segundos)
        return resultado

    def restaHora(self, h):
        """
        Devuelve el tiempo restado en xh xm xs
        :return suma de horas
        """

        return Tiempo(self.horas - h, self.minutos, self.segundos)

    def restaMinutos(self, m):
        """
        Devuelve el tiempo restado en xh xm xs
        :return suma de horas
        """
        segundos = self.toSegundos() - m * 60
        resultado = self.toHoras(segundos)

        return resultado

    def restaSegundos(self, s):
        """
        Devuelve el tiempo restado en xh xm xs
        :return suma de horas
        """
        segundos = self.toSegundos() - s
        resultado = self.toHoras(segundos)
        return resultado

if __name__ == "__main__":
    t1=Tiempo(5, 30, 99)
    t2=Tiempo(1, 1, 25)

    t3=t1.suma(t2)
    print("la suma del tiempo es:", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")
    t3=t1.resta(t2)
    print("la resta del tiempo es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")

    h=5
    t3=t1.sumaHora(h)
    print("la suma de", h, " horas es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")

    m=5
    t3=t1.sumaMinutos(m)
    print("la suma de", m, " minutos es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")

    s=5
    t3=t1.sumaSegundos(s)
    print("la suma de", s, " segundos es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")

    h = 5
    t3 = t1.restaHora(h)
    print("la resta de", h, " horas es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")

    m = 5
    t3 = t1.restaMinutos(m)
    print("la resta de", m, " minutos es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")

    s = 5
    t3 = t1.restaSegundos(s)
    print("la resta de", s, " segundos es: ", t3.horas, "h ", t3.minutos, "m ", t3.segundos, "s ")