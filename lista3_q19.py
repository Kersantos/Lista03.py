""" Lista3_q19. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o número de divisores desse valor.
"""

def divisores(num):
    if type(num) != int or num < 0:
        return Exception
    qtd = 0
    for div in range(1, num+1):
        if num % div == 0:
            qtd += 1
    return qtd


assert divisores(4) == 3
assert divisores(22) == 4
assert divisores(120) == 16
assert divisores(0) == 0
assert divisores(225) == 9
assert divisores(7) == 2
assert divisores(29) == 2
assert divisores('a') == Exception
assert divisores(-7) == Exception
assert divisores(2.8) == Exception
assert divisores(-7.8) == Exception
assert divisores(4.7) == Exception
assert divisores('moon') == Exception

print('Todos testes ok!')