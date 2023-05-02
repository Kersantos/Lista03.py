""" Lista3_q17. Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.
"""

import random

def maior_menor():
    valores = []
    for i in range(50):
        valor = random.randint(1, 100)
        valores.append(valor)
    

    maior = max(valores)
    menor = min(valores)

    return maior, menor, valores


maior, menor, valores = maior_menor()
print(f'valores {valores}')
print(f'\nMaior {maior}')
print(f'Menor {menor}')