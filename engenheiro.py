from classes1.interfaces.formas import FormasInterfaces
from typing import Type

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterfaces]):
        perimetro = terreno.get_perimetro()
        print('{} medio o perimetro: {} m'.format(self.nome, perimetro))

    def medir_area(self, terreno: Type[FormasInterfaces]):
        area = terreno.get_area()
        print('{} medio a area: {} m2'.format(self.nome, area))