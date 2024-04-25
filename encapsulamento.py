class Pessoa:
    def __init__(self,nome,idade, cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf ##não deve ser usando fora desta classe

    def correr(self):
        print('estou correndo')

    def beber(self,bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        else:
            print('bebendo ...')
        
    def __apresentar_documento(self): ##não deve ser usando fora desta classe
        print(self.__cpf)

fulano = Pessoa('fulano',23,15164531)
fulano.beber('cerveja')
fulano.beber('agua')
