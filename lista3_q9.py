""" Lista3_q9. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.
"""

def par_impar(n):
    if type(n) != int or n <= 0:
        return Exception
    if n % 2 == 0:
        return True
    else:
        return False

assert par_impar(2) == True
assert par_impar(8) == True
assert par_impar(14) == True
assert par_impar(66) == True
assert par_impar(68) == True
assert par_impar(9) == False
assert par_impar(13) == False
assert par_impar(455) == False
assert par_impar('c') == Exception
assert par_impar(-2.7) == Exception
assert par_impar(4.7) == Exception
assert par_impar(0) == Exception
assert par_impar(-7) == Exception
assert par_impar('einh') == Exception

print('Todos testes ok!')