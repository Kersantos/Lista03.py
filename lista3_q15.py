""" Lista3_q15. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.
"""

def estatisticas():
    salario_ttl = 0
    filhos_ttl = 0
    pessoas = 0
    maior_salario = 0
    salar_350 = 0

    while True:
        salario = float(input('Salario do habitante: (-1 para sair): '))
        if salario == -1:
            break

        filhos = int(input('Número de filhos do habitante: '))

        salario_ttl += salario
        filhos_ttl += filhos
        pessoas += 1

        if salario > maior_salario:
            maior_salario = salario
        if salario <= 350:
            salar_350 += 1
    media_salario = salario_ttl / pessoas
    media_filhos = filhos_ttl / pessoas
    perc_350 = (salar_350 / pessoas) * 100

    return media_salario, media_filhos, maior_salario, perc_350

medsa, medfi, maisa, perc_350 = estatisticas()

print(f'\nMédia de salário: R${medsa:.2f}')
print(f'Média de filhos: {medfi:.2f}')
print(f'Maior salário: R${maisa:.2f}')
print(f'Percentual de pessoas com salário até R$350,00: {perc_350:.2f}%')