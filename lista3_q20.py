""" Lista3_q20. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.
"""

def somatorio(num):
    if type(num) != int or num < 0:
        return Exception
    
    soma = 0
    for sum in range(1, num+1):
        soma += sum
    return soma

assert somatorio(7) == 28
assert somatorio(22) == 253
assert somatorio(4) == 10
assert somatorio(16) == 136
assert somatorio(2) == 3
assert somatorio(0) == 0
assert somatorio(5) == 15
assert somatorio('x') == Exception
assert somatorio('y') == Exception
assert somatorio(-7) == Exception
assert somatorio(-4.7) == Exception
assert somatorio(5.7) == Exception
assert somatorio(29.22) == Exception

print('Todos testes ok!')