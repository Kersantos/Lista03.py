""" Lista3_q25. Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o
seu fatorial.
"""

def fatorial(valor):
    if type(valor) != int or valor < 0:
        return Exception
    
    fat = 1
    for i in range(1, valor+1):
        fat *= i
    return fat

assert fatorial(0) == 1
assert fatorial(1) == 1
assert fatorial(2) == 2
assert fatorial(3) == 6
assert fatorial(4) == 24
assert fatorial(5) == 120
assert fatorial(6) == 720
assert fatorial('c') == Exception
assert fatorial(3.7) == Exception
assert fatorial(-2.9) == Exception
assert fatorial(-7) == Exception
assert fatorial('C') == Exception

print('Todos testes ok!')