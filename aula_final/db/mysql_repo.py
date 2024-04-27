from .interface1 import Repositorio


class MsySqlRepo(Repositorio):

    def inserir(sefl, dado) -> None:
        print('inserindo {} no banco mysql'.format(dado))

    def deletar(self, dado) -> None:
        print('deletando {} no banco mwsql'.format(dado))