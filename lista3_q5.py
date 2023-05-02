""" Lista3_q5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.
"""

def idade(anos, meses, dias):
    if type(anos) != int or type(meses) != int or type(dias) != int:
        return Exception
    if anos < 0 or meses < 0 or dias < 0:
        return Exception

    d_a = 365
    d_m = 30
    idd_d = (anos * d_a) + (meses * d_m) + dias

    return idd_d

assert idade(16, 7, 12) == 6062 # Testando classe válida
assert idade(19, 3, 13) == 7038 # Testando classe válida
assert idade(15, 3, 29) == 5594 # Testando classe válida
assert idade('a', 2, 6) == Exception # Testando classes inválidas
assert idade('u', 'o', 'l') == Exception # Testando inválidos
assert idade(-5, 46, 1) == Exception # Testando classes inválidas
assert idade(-9, -6, 0) == Exception # Testando classes inválidas
assert idade('p', 3, 'o') == Exception # Testando classes inválidas

print('Todos testes estão ok!')