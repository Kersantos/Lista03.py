""" Lista3_q7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna a categoria desse nadador de acordo com a tabela abaixo.
    
    Idade             | Categoria
    5 a 7 anos        | Infantil A
    8 a 10 anos       | Infantil B
    11-13 anos        | Juvenil A
    14-17 anos        | Juvenil B
    Maiores de 18 anos| Adulto
    (inclusive)       |
"""

def idade(idd):
    if type(idd) != int or idd >= 120:
        return Exception
    if idd <= 0:
        return Exception
    if idd >= 5 and idd <= 7:
        return f'Infantil A'
    elif idd >= 8 and idd <= 10:
        return f'Infantil B'
    elif idd >= 11 and idd <= 13:
        return f'Juvenil A'
    elif idd >= 14 and idd <= 17:
        return f'Juvenil B'
    else:
        return f'Adulto'

assert idade(0) == Exception
assert idade('c') == Exception
assert idade(4.7) == Exception
assert idade(-2) == Exception
assert idade(157) == Exception
assert idade(5) == 'Infantil A'
assert idade(7) == 'Infantil A'
assert idade(8) == 'Infantil B'
assert idade(10) == 'Infantil B'
assert idade(11) == 'Juvenil A'
assert idade(13) == 'Juvenil A'
assert idade(14) == 'Juvenil B'
assert idade(16) == 'Juvenil B'
assert idade(17) == 'Juvenil B'
assert idade(18) == 'Adulto'
assert idade(47) == 'Adulto'
assert idade(22) == 'Adulto'

print('Todos testes ok!')