class ControleRemoto:

    def __init__(self, televisao, comodo) -> None:
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('canal avancado')

    def voltar_canal(self):
        print('voltar canal')

    def escolher_canal(self, canal):
        print('canal selecionado {}'.format(canal))


controle_sala = ControleRemoto('lg','sala')
tv = controle_sala.televisao
comodo = controle_sala.comodo
print(tv)
print(comodo)
controle_sala.avancar_canal()
canal_select = controle_sala.escolher_canal(5)
print(canal_select)