"""Lista3_q8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.
"""

def positivo_negativo(n):
    if type(n) != int:
        return Exception
    if n >= 0:
        return True
    else:
        return False
    
assert positivo_negativo('c') == Exception
assert positivo_negativo(-2.3) == Exception
assert positivo_negativo(2.9) == Exception
assert positivo_negativo(-3) == False
assert positivo_negativo(-18) == False
assert positivo_negativo(0) == True
assert positivo_negativo(22) == True
assert positivo_negativo(152) == True
assert positivo_negativo(-7) == False

print('Todos testes ok!')