from abc import ABC, abstractmethod


class Repositorio(ABC):

    @abstractmethod
    def inserir(sefl, dado) -> None:
        pass

    @abstractmethod    
    def deletar(self, dado) -> None:
       pass