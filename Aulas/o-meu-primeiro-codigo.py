#importação de biblioteca
import math

# Definiçao de funçao
def calcular_area_retangulo(l, a):
    """Calcular a área de um retângulo"""
    return l * a

#codigo principal
#definir as dimensões do retângulo
largura = 12.5
altura = 10

# chamada de função para calcular a área
area = calcular_area_retangulo(largura, altura)

#imprimindo o resultado
print(f"A área do retângulo é {area}")

