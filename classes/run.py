from abs_class import *

class Filha(ClassAbstrata):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self):
        print("Implementando metodo abstrato")


filha = Filha()
filha.apresentar_metodo()
filha.metodo("Estou aqui!")
filha.metodo_abstrato()

#erro
# class_abstrata = ClassAbstrata()
# class_abstrata.metodo("faz algo")