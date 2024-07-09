# Exemplo de representação de matriz com listas de listas
matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# Acessando elementos em uma matriz
matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
elemento = matriz[1][2] # Acessando o elemento na segunda linha e terceira coluna (6)

# Exemplo de uso do NumPy para trabalhar com matrizes
import numpy as np # type: ignore
# Criando matrizes usando NumPy
matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# Adição de matrizes
soma = matriz_a + matriz_b
# Multiplicação por um escalar
escalar = 2
resultado = escalar * matriz_a
# Multiplicação de matrizes
produto = np.dot(matriz_a, matriz_b)
# Transposição de matriz
transposta = matriz_a.T


# Exemplo 1: Conversão de um valor numérico para inteiro
valor_float = 3.14
inteiro = int(valor_float) # Resultado: 3
# Exemplo 2: Conversão de uma string para inteiro
valor_string = "42"
inteiro = int(valor_string) # Resultado: 42

# Exemplo 1: Conversão de uma string para lista de caracteres
texto = "Python"
lista_caracteres = list(texto) # Resultado: ['P', 'y', 't', 'h', 'o', 'n']
# Exemplo 2: Conversão de uma tupla para lista
tupla = (1, 2, 3)
lista = list(tupla) # Resultado: [1, 2, 3]


