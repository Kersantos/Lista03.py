""" Lista3_q6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.
"""

def perfeito(n):
    if type(n) != int:
        return Exception
    if n < 0:
        return Exception
    
    soma = 0 
    for div in range(1, n):
        if n % div == 0:
            soma += div
    if soma == n:
        return True
    else:
        return False

assert perfeito(6) == True # Testando classe válida
assert perfeito(28) == True # Testando classe válida
assert perfeito(496) == True # Testando classe válida
assert perfeito(8128) == True # Testando classe válida
assert perfeito(11) == False # Testando classe válida
assert perfeito(78) == False # Testando clase válida
assert perfeito(27) == False # Testando classe válida
assert perfeito(3) == False # Testando classe válida
assert perfeito(-1) == Exception # Testando valor improvável
assert perfeito(-3) == Exception # Testando valor improvável
assert perfeito('u') == Exception # Testando valor improvável
assert perfeito(4.7) == Exception # Testandovalor improvável
assert perfeito(5.8) == Exception # Testandovalor improvável

print('Todos testes estão ok!')