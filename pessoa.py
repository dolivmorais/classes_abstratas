class Pessoa:

    def __init__(self,nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print('dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None:
        print('lalala')

    def apresentar_idade(self) -> int:
        return self.idade
    
    