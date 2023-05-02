""" Lista3_q11. Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal. Para homens, calcular o peso usando a fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura - 44.7.
"""

def peso_ideal(altura, sexo):
    if type(altura) != float or altura <= 0:
        return Exception
    if type(sexo) != str:
        return Exception
    if sexo != 'M' and sexo != 'F':
        return Exception

    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7

    return round(peso_ideal, 2)

assert peso_ideal(-2, 5) == Exception
assert peso_ideal(0, 'M') == Exception
assert peso_ideal('A', -7) == Exception
assert peso_ideal('F', 'M') == Exception
assert peso_ideal(9.3, 10) == Exception
assert peso_ideal(1.70, 2) == Exception
assert peso_ideal(1.70, 'M') == 65.59
assert peso_ideal(1.75, 'M') == 69.23
assert peso_ideal(1.82, 'M') == 74.31
assert peso_ideal(1.65, 'F') == 57.77
assert peso_ideal(1.60, 'F') == 54.66
assert peso_ideal(1.72, 'F') == 62.11
assert peso_ideal(1.59, 'F') == 54.04
assert peso_ideal(160, 'F') == Exception
assert peso_ideal(1.90, 'I') == Exception

print('Todos testes ok!')