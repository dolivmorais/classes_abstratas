
class Calculadora:

    def calcular(op: str, n1: float, n2: float):

        if op == "+":
            soma = n1 + n2
            print(soma)
        elif op == "-":
            subtracao = n1 -  n2
            print(subtracao)
        elif op == "/":
            if n1 == 0 or n2 == 0:
                print('divisao por zero')
            divisao = n1 / n2
            print(divisao)
        elif op == "*":
            multiplicao = n1 * n2
            print(multiplicao)
        else:
            print('operação invalida!')


calculo = Calculadora.calcular("-",20,2)

        