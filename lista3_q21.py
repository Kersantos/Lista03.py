""" Lista3_q21. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
"""

def calcular(valor):
    if type(valor) != int or valor < 0:
        return Exception

    s = 0
    for b in range(1, valor+1):
        s += 1/b
    return round(s, 2)

assert calcular(5) == 2.28
assert calcular(8) == 2.72
assert calcular(17) == 3.44
assert calcular(25) == 3.82
assert calcular(91) == 5.09
assert calcular(2) == 1.50
assert calcular(4) == 2.08
assert calcular(0) == 0
assert calcular('x') == Exception
assert calcular('F') == Exception
assert calcular(-2) ==  Exception
assert calcular(-3.7) == Exception
assert calcular(7.4) == Exception
assert calcular(True) == Exception
assert calcular(False) == Exception


print('Todos testes ok!')