'''Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.'''
def primo(n):
    if type(n) != int:
        return Exception
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

assert primo(2) == True # Testando classe válida
assert primo(0) == False # Testando classe válida
assert primo(-4) == False # Testando classe válida
assert primo(1) == False # Testando classe válida
assert primo(3) == True # Testando classe válida
assert primo(11) == True # Testando classe válida
assert primo(29) == True # Testando classe válida
assert primo(31) == True # Testando classe válida
assert primo(47) == True # Testando classe válida
assert primo('ein') == Exception # Valor improvável
assert primo(5.6) == Exception # Valor improvável
assert primo(8.9) == Exception # Valor improvável

print('Todos testes estão ok!')
