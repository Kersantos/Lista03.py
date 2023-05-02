"""Lista3_q1. Faça uma função que recebe por parâmetro o raio de uma esfera
e calcula o seu volume (v = 4/3 * PI  * R**3)."""
def volume(raio):
    if type(raio) == str:
        return Exception
    if raio <= 0:
        return Exception
    return round(4/3 * 3.14 * raio**3,2)

assert volume(1.0) == 4.19, "Deveria retornar 4.19"    # testando classe válida
assert volume(1) == 4.19    # testando classe válida
assert volume(0) == Exception  #testando valor improvável
assert volume(-1) == Exception  # testando valor improvável
assert volume('abc') == Exception  # testando valor inválido
print("Todos os testes ok!")