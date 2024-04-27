
from classes1.terrenos.quandrado import TerrenoQuadrado
from classes1.terrenos.retangulo import TerrenoRetangular
from engenheiro import Engenheiro


engenheiro = Engenheiro('Diego')
Terreno_Quadrado = TerrenoQuadrado(4)
Terreno_Retangular = TerrenoRetangular(2,3)

engenheiro.medir_area(Terreno_Quadrado)
engenheiro.medir_area(Terreno_Retangular)


