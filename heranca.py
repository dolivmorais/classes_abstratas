class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'silva'

    def comer(self) -> None:
        print('estoui comendo ...')

    def estudar(self) -> None:
        print('estudando ...')

class Filha(Mae):
    
    def __init__(self, endereco):
        super().__init__(endereco)

    def brincar(self, brinquedo) -> None:
        print('estou bincando com {}'.format(brinquedo))

class Neta(Filha):
     
     def __init__(self, endereco):
         super().__init__(endereco)


ana = Mae('Rua Um')
clara = Filha('Rua dois')
clara.brincar('carrinho')

print(ana.endereco)
print(clara.endereco)


