# Exemplos de listas
lista_numeros = [1, 2, 3, 4, 5]
lista_frutas = ['maçã', 'banana',
'laranja']
lista_mista = [10, 'python', True]

# Exemplo de acesso a elementos em uma lista
numeros = [10, 20, 30, 40, 50]
primeiro_elemento = numeros[0] # 10
segundo_elemento = numeros[1] # 20
ultimo_elemento = numeros[-1] # 50 (último elemento da lista)

# Exemplos de operações com listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
# Adição de elementos
lista_a.append(4) # [1, 2, 3, 4]
lista_b.insert(0, 0) # [0, 4, 5, 6]
# Remoção de elementos
lista_a.remove(2) # [1, 3]
elemento_removido = lista_b.pop(2) # elemento_removido = 5, lista_b = [0,4, 6]
# Concatenação de listas
lista_concatenada = lista_a + lista_b # [1, 3, 0, 4, 6]
# Fatiamento (slicing)
sublista = lista_concatenada[1:4] # [3, 0, 4]


# Exemplos de funções úteis para listas
numeros = [5, 2, 8, 1, 9]
tamanho = len(numeros) # Retorna o tamanho da lista (5)
maior = max(numeros) # Retorna o maior valor (9)
menor = min(numeros) # Retorna o menor valor (1)
soma_total = sum(numeros) # Retorna a soma dos elementos (25)