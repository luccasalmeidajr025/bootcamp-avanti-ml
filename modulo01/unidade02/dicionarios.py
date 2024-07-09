# Exemplos de dicionários
dicionario_pessoas = {
'nome': 'João',
'idade': 30,
'cidade': 'São Paulo'
}
dicionario_notas = {
'Matemática': 9.5,
'Ciências': 8.0,
'História': 7.5
}

# Exemplo de acesso a elementos em um dicionário
pessoa = {
'nome': 'Maria',
'idade': 25,
'cidade': 'Rio de Janeiro'
}
nome = pessoa['nome'] # 'Maria'
idade = pessoa['idade'] # 25
cidade = pessoa['cidade'] # 'Rio de Janeiro'

# Exemplo de operações com dicionários
pessoa = {
'nome': 'João',
'idade': 30,
'cidade': 'São Paulo'
}

#Adicionar novo elemento
pessoa['profissao'] = 'Engenheiro'

# Modificar valor associado a uma chave
pessoa['idade'] = 31

# Remover elemento
del pessoa['cidade']

# Exemplos de funções úteis para dicionários
pessoa = {
'nome': 'João',
'idade': 30,
'cidade': 'São Paulo'
}
tamanho = len(pessoa) # Retorna o número de pares chave-valor (3)
chaves = pessoa.keys() # Retorna as chaves do dicionário ('nome', 'idade', 'cidade')
valores = pessoa.values() # Retorna os valores do dicionário ('João', 30, 'São Paulo')
pares = pessoa.items() # Retorna uma lista de tuplas com os pares chave-valor