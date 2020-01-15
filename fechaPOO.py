class Fecha:
    """
    1. fechaCorrecta: dice si la fecha que se pasa como parámetro es correcta.
    2. fechaMas1Dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
    3. fechaMasNDias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    4. fechaMenos1Dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
    5. fechaMenosNDias: resta una serie de días a la fecha que se pasa como  parámetro y lo devuelve.
    6. esBisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
    7. comparaFechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la segunda,
     cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
    8. fechaFormateada: recibe un fecha y devuelve una cadena con el formato: DD
    de {MES} de AAAA (Ejemplo: "15 de Diciembre de 2019")
    9. anyo, mes, dia, nombreMes: recibe un fecha y devuelve esos valores.
    """

    def __init__(self, fecha):
        """
        Constructor de la clase
        :param base: base del rectángulo
        :param altura: altura del rectángulo
        """
        self.fecha=fecha
        self.dia = int(self.fecha) % 100
        self.mes = int(self.fecha)//100 % 100
        self.anyo = int(self.fecha)//10000


    def fechaCorrecta(self):
        f1=Fecha(self.fecha)
        fechaBien = True
        if not (len(self.fecha) == 8 and self.fecha[:8].isdecimal()):
            return False
        day = self.dia
        month = self.mes

        # comprobamos si el mes esta bien
        if 0 > month > 12:
            fechaBien = False
        # comprobamos que los dias esten bien según el mes
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 0 or day > 31:
                fechaBien = False
        elif month == 2:
             if f1.esBisiesto():
                if day > 29:
                   fechaBien = False
             else:
               if day > 28:
                    fechaBien = False
        else:
            if day > 30:
                fechaBien = False

        return fechaBien

    def esBisiesto(self):
        return (self.anyo % 100 != 0 or self.anyo % 400 == 0) and self.anyo % 4 == 0

    def nombreMes(self, mes):
        mess = mes

        if mess == 1:
            mesLetra = "enero"
        elif mess == 2:
            mesLetra = "febrero"
        elif mess == 3:
            mesLetra = "marzo"
        elif mess == 4:
            mesLetra = "abril"
        elif mess == 5:
            mesLetra = "mayo"
        elif mess == 6:
            mesLetra = "Junio"
        elif mess == 7:
            mesLetra = "Julio"
        elif mess == 8:
            mesLetra = "Agosto"
        elif mess == 9:
            mesLetra = "Septiembre"
        elif mess == 10:
            mesLetra = "octubre"
        elif mess == 11:
            mesLetra = "noviembre"
        elif mess == 12:
            mesLetra = "diciembre"
        else:
            mesLetra = "mes erroneo"

        return mesLetra

    def fechaFormateada(self):
        day = self.dia
        year = self.anyo
        month=self.mes
        fechaLetra = ""
        fechaLetra += str(day) + " del " + self.nombreMes(month) + " de " + str(year)

        return fechaLetra


    def fechaMas1Dia(self):
        f1 = Fecha(self.fecha)
        day = self.dia
        month = self.mes
        year = self.anyo

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
            if day == 31:
                month += 1
                day = 1
            else:
                day += 1
        elif month == 2:
            if f1.esBisiesto():
                if day == 29:
                    month += 1
                    day = 1
                else:
                    day += 1
            else:
                if day == 28:
                    month += 1
                    day = 1
                else:
                    day += 1
        elif month == 12:
            if day == 31:
                year += 1
                month = 1
                day = 1
            else:
                day += 1
        else:
            if day == 30:
                day += 1
            else:
                month += 1
                day = 1

        return Fecha(f"{year:04}{month:02}{day:02}")

    def fechaMasNDias(self, dias):
        f1 = Fecha(self.fecha)
        for i in range(1, dias):
            f1=f1.fechaMas1Dia()
        return f1

    def fechaMenos1Dia(self):
        day = self.dia
        month = self.mes
        year = self.anyo
        f1 = Fecha(self.fecha)

        if day == 1:
            month = month - 1
            if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                day = 31

            elif month == 2:
                if f1.esBisiesto():
                    day = 29
                else:
                    day = 28
            elif month == 1:
                year = year - 1
                month = 12
                day = 31
            else:
                day = 30
        else:
            day = day - 1

        return Fecha(f"{year:04}{month:02}{day:02}")

    def fechaMenosNDias(self, dias):
        f1 = Fecha(self.fecha)
        for i in range(1, dias):
            f1 = f1.fechaMenos1Dia()
        return f1

    def comparaFechas(self, fecha2):
        day1 = self.dia
        month1 = self.mes
        year1 = self.anyo

        day2 = fecha2.dia
        month2 = fecha2.mes
        year2 = fecha2.anyo

        if year1 < year2:
            return -1
        elif year1 > year2:
            return 1
        else:
            if month1 < month2:
                return -1
            elif month1 > month2:
                return 1
            else:
                if day1 < day2:
                    return -1
                elif day1 > day2:
                    return 1
                else:
                    return 0


if __name__ == "__main__":
    fechas = ("20191215", "20181111",  "20181242", "20010229", "20000229")

    for f in fechas:
        f1=Fecha(f)
        if f1.fechaCorrecta():
            print("CORRECTO")
        else:
            print("INCORRECTO")

    fecha1 = Fecha("20160228")
    fecha2 = Fecha("20160301")
    fecha3 = Fecha( "20170228")
    fecha4 = Fecha("20170301")

    print("Si suma un día" + fecha1.fechaFormateada() + "' obtenemos: " + fecha1.fechaMas1Dia().fechaFormateada())
    print("Si restamos un día a '" + fecha2.fechaFormateada() + "' obtenemos: " + fecha2.fechaMenos1Dia().fechaFormateada())
    print("Si sumamos un día a '" + fecha3.fechaFormateada() + "' obtenemos: " + fecha3.fechaMas1Dia().fechaFormateada())
    print("Si restamos un día a '" + fecha4.fechaFormateada() + "' obtenemos: " + fecha4.fechaMenos1Dia().fechaFormateada())

    print("")



    suma = int(input("Indique cuantos días quieres sumar a "+ fecha1.fechaFormateada()))
    print("La fecha resultante es " + fecha1.fechaMasNDias(suma).fechaFormateada())

    resta = int(input("Indique cuantos días quieres restar a " + fecha1.fechaFormateada()))
    print("La fecha resultante es " + fecha1.fechaMenosNDias(resta).fechaFormateada())


    fecha2 = Fecha("20160120")
    fecha3 = Fecha("20190101")

    print("El resultado de comparar '" + fecha1.fechaFormateada() + "' con '" + fecha2.fechaFormateada() + "' es " + str(fecha1.comparaFechas(fecha2)))

    print("El resultado de comparar '" + fecha1.fechaFormateada() + "' con '" + fecha3.fechaFormateada() + "' es " + str(fecha1.comparaFechas(fecha3)))

    print("El resultado de comparar '" + fecha3.fechaFormateada() + "' con '" + fecha2.fechaFormateada() + "' es " + str(fecha3.comparaFechas(fecha2)))

    print("El resultado de comparar '" + fecha3.fechaFormateada() + "' con '" + fecha3.fechaFormateada() + "' es " + str(fecha3.comparaFechas(fecha3)))
