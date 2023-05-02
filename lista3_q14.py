""" Lista3_q14. Escreva uma função que recebe 3 valores reais X, Y e Z que verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois lados. O procedimento deve identificar o tipo de triângulo formado observando as seguintes definições:
        - Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
        - Triângulo Isósceles: os comprimentos de 2 lados são iguais.
        - Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.
"""

def triangulo(x, y, z):
    if type(x) != float and type(x) != int or type(y) != float and type(y) != int or type(z) != float and type(z) != int:
        return Exception
    if x < 0 or y < 0 or z <0:
        return Exception
    if x < y + z and y < x + z and z < x + y:
        if x == y and y == z:
            return 'Equilátero'
        elif x == y or x == z or y == z:
            return 'Isósceles'
        else:
            return 'Escaleno'


assert triangulo(4.7, 4.7, 4.7) == 'Equilátero'
assert triangulo(3, 3, 3) == 'Equilátero'
assert triangulo(6.8, 6.8, 8.9) == 'Isósceles'
assert triangulo(7, 7, 6) == 'Isósceles'
assert triangulo(3.4, 6.2, 6.2) == 'Isósceles'
assert triangulo(7.6, 7.7, 7.8) == 'Escaleno'
assert triangulo(7, 8, 9) == 'Escaleno'
assert triangulo('a', 3.9, 'b') == Exception
assert triangulo(9.4, 'a', 'p') == Exception
assert triangulo('o', 8, 9.8) == Exception
assert triangulo(-2, 8, -3.5) == Exception
assert triangulo(-1, -2, -3) == Exception

print('Todos testes ok!')