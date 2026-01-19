'''
Desenvolva uma classe Temperatura que armazene a temperatura em graus Celsius como um atributo privado.
Implemente um getter e um setter usando property para permitir que a
temperatura seja ajustada e lida em Celsius,
e adicione métodos para converter a temperatura para Fahrenheit e Kelvin.
'''

class Temperatura:
    def __init__(self, temperatura):
        self.__celcius = temperatura
        self.__kelvin = self.__converte_kelvin()
        self.__fahrenheit = self.__converte_fahrenheit()

    def __converte_kelvin(self):
        return self.__celcius + 273.15

    def __converte_fahrenheit(self):
        return (self.__celcius * 9 / 5) + 32

    @property
    def celcius(self):
        return self.__celcius

    @celcius.setter
    def celcius(self, temperatura):
        self.__celcius = temperatura
        self.__kelvin = self.__converte_kelvin()
        self.__fahrenheit = self.__converte_fahrenheit()

    @property
    def kelvin(self):
        return self.__kelvin

    @kelvin.setter
    def kelvin(self, temperatura):
        self.__celcius = temperatura - 273.15
        self.__kelvin = self.__converte_kelvin()
        self.__fahrenheit = self.__converte_fahrenheit()

    @property
    def fahrenheit(self):
        return self.__fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, temperatura):
        self.__celcius = (temperatura - 32) * 5 / 9
        self.__kelvin = self.__converte_kelvin()
        self.__fahrenheit = self.__converte_fahrenheit()

    def mostrar(self):
        return f'CELCIUS: {self.__celcius}ºC \n KELVIN: {self.__kelvin}ªK \n FAHRENHEIT: {self.__fahrenheit}ºF '
