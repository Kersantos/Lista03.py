""" Lista3_q13. Faça uma função que recebe por parâmetro, a hora de inicio e a hora de término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar, também por parâmetro, a duração do jogo em horas e minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.
"""

def duracao_jogo(hi, mi, ht, mt):
    if type(hi) != int or type(mi) != int or type(ht) != int or type(mt) != int:
        return Exception
    if hi < 0 or mi < 0 or ht < 0 or mt <0:
        return Exception
    if ht < hi:
        ht += 24
    dh = ht - hi
    dm = mt - mi

    if dm < 0:
        dh -= 1
        dm += 60
    if dh >= 24:
        dh -= 24

    return dh, dm

assert duracao_jogo(14, 30, 18, 45) == (4, 15)
assert duracao_jogo(21, 45, 3, 10) == (5, 25)
assert duracao_jogo(8, 30, 8, 30) == (0, 0)
assert duracao_jogo(20, 0, 22, 30) == (2, 30)
assert duracao_jogo('a', 23, 'd', 35) == Exception
assert duracao_jogo('a', 'b', 'c', 'd') == Exception
assert duracao_jogo(1.2, 8, 22.3, 8) == Exception
assert duracao_jogo(-7, 30, 22, -6) == Exception

print('Todos testes ok!')