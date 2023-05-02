""" Lista3_q16. Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos.
"""

def media_aritmetica():
    s = 0
    qtd = 0

    while True:
        valor = float(input('Digite um valor positivo (-1 para sair): '))

        if valor == -1:
            break

        s += valor
        qtd += 1

    if qtd == 0:
        return 0
    
    media_aritmetica = s / qtd

    return media_aritmetica

print(f'A média aritmética dos valores digitados é {media_aritmetica()}')