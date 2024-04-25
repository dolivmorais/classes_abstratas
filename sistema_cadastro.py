class SistemaCadastral:

    # principio da responsabilidade unica
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
           self.__armazenar_usuario(nome, idade) 
        else:
            self.__indicar_erro

    def __verificar_dados(self, nome: str, idade: int) -> bool: ## privado
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
        
    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('acesando o banco de dados...')
        print('cadastrando o usuario {}, Idade'.format(nome, idade))

    def __indicar_erro(self):
        print('dados são inválidos')

chamada = SistemaCadastral()
sis = chamada.cadastrar('diego',33)
print(sis)