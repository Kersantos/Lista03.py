""" Lista3_q10. Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo.
    Nota         | Conceito
    de 0,0 a 4,9 | D
    de 5,0 a 6,9 | C
    de 7,0 a 8,9 | B
    de 9,0 a 10,0| A
"""

def media_final(med):
    if type(med) != int and type(med) != float:
        return Exception
    if med < 0 or med > 10:
        return Exception
    
    if med >= 0.0 and med <= 4.9:
        return 'D'
    elif med >= 5.0 and med <= 6.9:
        return 'C'
    elif med >= 7.0 and med <= 8.9:
        return 'B'
    elif med >= 9.0 and med <= 10.0:
        return 'A'
    
assert media_final(0.0) == 'D'
assert media_final(4.9) == 'D'
assert media_final(3.6) == 'D'
assert media_final(6.4) == 'C'
assert media_final(5.9) == 'C'
assert media_final(6.9) == 'C'
assert media_final(7.1) == 'B'
assert media_final(7.3) == 'B'
assert media_final(8.9) == 'B'
assert media_final(9.2) == 'A'
assert media_final(9.9) == 'A'
assert media_final(10.0) == 'A'
assert media_final(-2) == Exception
assert media_final(-4.7) == Exception
assert media_final('A') == Exception
assert media_final(11) == Exception
assert media_final(17) == Exception
assert media_final('I') == Exception

print('Todos testes ok!')