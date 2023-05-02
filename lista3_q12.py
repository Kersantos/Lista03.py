""" Lista3_q12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.
"""

def crescente(valor1, valor2):
    if type(valor1) != int or type(valor2) != int:
        return Exception
    if valor1 > valor2:
        return valor2, valor1
    else:
        return valor1, valor2
    

assert crescente('a', 2) == Exception
assert crescente('b', 'i') == Exception
assert crescente(3, 'j') == Exception
assert crescente(5, 2) == (2, 5)
assert crescente(10, 8) == (8, 10)
assert crescente(1, 82) == (1, 82)
assert crescente(452, 123) == (123, 452)
assert crescente(2.3, 69) == Exception
assert crescente(67, 4.7) ==Exception

print('Todos testes ok!')