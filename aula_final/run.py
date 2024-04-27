from typing import Type
from db.interface1 import Repositorio
from db.mongo_repo import MongolRepo
from db.mysql_repo import MsySqlRepo

class Usuario:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio

    def armazenar_dado(self, dado: any) -> None:
        self.__repositorio.inserir(dado)

    def deletar_dado(self, dado: any) -> None:
        self.__repositorio.deletar(dado)


usuario = Usuario(MongolRepo())

usuario.armazenar_dado(23)

usuario = Usuario(MsySqlRepo())

usuario.armazenar_dado(25)