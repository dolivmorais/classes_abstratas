from typing import Type

class Animal:

    def comer(self):
        print('o animal esta comendo')

    def dormir(self):
        print('o animal esta dormindo')

    def andar(self):
        print('o animal esta dormindo')


class Aves(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self):
        print('a ave esta cantando')


class Pinguim(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self):
        print('o oinguim esta escorregando no gelo')


class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.comer()


diego = Pessoa()
pinguim = Pinguim()
diego.observar(pinguim) 


    