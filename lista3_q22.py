""" Lista3_q22. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
"""

def calcular(valor):
    if type(valor) != int or valor < 0:
        return Exception
    
    s = 1
    fat = 1
    for i in range(1, valor+1):
        fat *= i
        s += 1/fat
    return round(s, 3)

assert calcular(0) == 1
assert calcular(1) == 2.0
assert calcular(2) == 2.5
assert calcular(5) == 2.717
assert calcular(10) == 2.718
assert calcular('x') == Exception
assert calcular('Y') == Exception
assert calcular(-2) == Exception
assert calcular(-5.4) == Exception
assert calcular(4.7) == Exception
assert calcular(True) == Exception
assert calcular(False) == Exception

print('Todos testes ok!')