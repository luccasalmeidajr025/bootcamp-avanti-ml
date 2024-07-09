# Operações com listas
numeros = [1, 2, 3]
# Adicionar elemento ao final da lista
numeros.append(4) # números agora é [1, 2, 3, 4]
# Remover elemento específico da lista
numeros.remove(2) # números agora é [1, 3, 4]
# Verificar o tamanho da lista
tamanho = len(numeros) # tamanho é 3
# Concatenar duas listas
outra_lista = [5, 6, 7]
concatenada = numeros + outra_lista # concatenada é [1, 3, 4, 5, 6, 7]


frutas = ['maçã', 'banana', 'laranja']
del frutas[1] # Remove o elemento na posição 1 (banana)
print(frutas) # Saída: ['maçã', 'laranja']

pessoas = {'João': 25, 'Maria': 30, 'Pedro': 22}
del pessoas['Maria']
print(pessoas) # Saída: {'João': 25, 'Pedro': 22




# Exemplo 1: Conjunto com chaves {}
frutas = {'maçã', 'banana', 'laranja'}
# Exemplo 2: Conjunto com a função set()
numeros = set([1, 2, 3, 4, 5])

conj1 = {1, 2, 3}
conj2 = {3, 4, 5}
# Adicionar elemento
conj1.add(4) # conj1 agora é {1, 2, 3, 4}
# Remover elemento
conj1.remove(2) # conj1 agora é {1, 3, 4}
# Verificar a existência de um elemento
if 3 in conj1:
    print("O número 3 está no conjunto conj1.")
# União de conjuntos
uniao = conj1.union(conj2) # uniao é {1, 3, 4, 5}
# Interseção de conjuntos
intersecao = conj1.intersection(conj2) # intersecao é {3}
# Diferença entre conjuntos
diferenca = conj1.difference(conj2) # diferenca é {1, 4}


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# Resultado
#gallahad the pure
#robin the brave