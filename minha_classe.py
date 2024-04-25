class MinhaClasse:

    def __init__(self,att) -> None: ##metodo construtor
        self.meu_atributo = "Olá mundo!"
        self.meu_atributo2 = att

    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, n1, n2):
        return n1 * n2
    

objeto = MinhaClasse(2)

objeto.meu_metodo()

