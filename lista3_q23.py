""" Lista3_q23. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)
"""

def calcular(valor):
    if type(valor) != int or valor < 0:
        return Exception
    
    s = 0
    for i in range(1, valor+1):
        n = i**2 + 1
        d = i + 3
        t = n / d
        s += t
    return round(s, 2)

assert calcular(2) == 1.5
assert calcular(0) == 0
assert calcular(8) == 23.87
assert calcular(5) == 8.85
assert calcular(3) == 3.17
assert calcular(10) == 38.47
assert calcular(-4.7) == Exception
assert calcular(2.9) == Exception
assert calcular(-3) == Exception
assert calcular('C') == Exception
assert calcular('j') == Exception
assert calcular(True) == Exception
assert calcular(False) == Exception

print('Todos testes ok!')