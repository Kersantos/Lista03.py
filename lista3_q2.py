"""Lista3_q2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro
e uma letra. Se a letra for A o procedimento calcula a média aritmética das
notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2).
A função deve retornar a média calculada."""
def calcular_media(n1,n2,n3,letra):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float) or (type(n3) != int and type(n3) != float):
        return Exception
    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        return Exception
    if letra == "A":
        return (n1 + n2 + n3) / 3
    elif letra == "P":
        return (n1*5 + n2*3 + n3*2) / 10
    else:
        return Exception

assert calcular_media("x",4,5.0,"X") == Exception
assert calcular_media(3,4,5,"X") == Exception
assert calcular_media(3,4,5,"a") == Exception
assert calcular_media("A",4,5,"P") == Exception
assert calcular_media(3,4,5,6) == Exception
assert calcular_media(30,4,5,"A") == Exception
assert calcular_media(3,40,5,"A") == Exception
assert calcular_media(3,4,50,"A") == Exception
assert calcular_media(30,4,5,"P") == Exception
assert calcular_media(3,40,5,"P") == Exception
assert calcular_media(3,4,50,"P") == Exception
assert calcular_media(True,4,4,"A") == Exception
assert calcular_media(3,4,5,"A") == 4
assert calcular_media(3.5,3.5,5,"A") == 4.0
assert calcular_media(0,8,10,"A") == 6
assert calcular_media(3,4,5,"P") == 3.7

print("Testes ok!")