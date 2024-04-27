class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    @classmethod
    def vender(csl) -> int:
        return 40 * csl.tarifa
    
    @classmethod
    def alterar_tarifa(csl, novo_tarifa: int) -> None:
        csl.tarifa = novo_tarifa


lj1 = Loja("Centro")
lj2 = Loja("Praia")
lj1_end = lj1.apresentar_endereco()
lj2_end = lj2.apresentar_endereco()

print(lj1_end)
print(lj2_end)
print(lj1.vender())
print(lj2.vender())


print(lj2.alterar_tarifa(2.3))

print(lj1.vender())
print(lj2.vender())


