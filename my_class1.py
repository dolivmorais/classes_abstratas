from typing import Type

class Interruptor:

    def __init__(self,comodo: str) -> None:
        self.__comodo = comodo

    def acender(self):
        print('acendendo {}'.format(self.__comodo))

    def apagar(self):
        print('apagar {}'.format(self.__comodo))

class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        self.apagar_luz()

    def dormir(self):
        print('dormindo ...')

a = Pessoa()
Interruptor_quarto = Interruptor('quarto')

Interruptor_quarto.acender()
a.acender_luz(Interruptor_quarto)
