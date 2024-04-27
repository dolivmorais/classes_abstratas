from .interface1 import Repositorio


class MongolRepo(Repositorio):

    def inserir(sefl, dado) -> None:
        print('inserindo {} no banco mongo'.format(dado))

    def deletar(self, dado) -> None:
        print('deletando {} no banco mongo'.format(dado))