""" Lista3_q24. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula
e retorna Xz
. (sem utilizar funções ou operadores de potência prontos)
"""

def calcular(valor1, valor2):
    if type(valor1) != int and type(valor1) != float or type(valor2) != int:
        return Exception
    
    poten = 1
    for i in range(valor2):
        poten *= valor1
    return poten

assert calcular(2, 3) == 8
assert calcular(3, 4) == 81
assert calcular(5, 0) == 1
assert calcular(7, 2) == 49
assert calcular(56, 0) == 1
assert calcular(10, 4) == 10000
assert calcular(2.5, 2) == 6.25
assert calcular(5.5, 2) == 30.25
assert calcular(4, 2.5) == Exception
assert calcular(4.4, 2.3) == Exception
assert calcular('c', 2) == Exception
assert calcular(2, 'c') == Exception
assert calcular('c', 'j') == Exception
assert calcular(-2, 3) == -8

print('Todos testes ok!')