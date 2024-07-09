# Exemplos de strings
string1 = 'Olá, mundo!'
string2 = "Python é incrível!"
string3 = '''Strings em Python são flexíveis e poderosas.'''

# Exemplo de acesso a caracteres em uma string
mensagem = "Python"
primeiro_caracter = mensagem[0] # 'P'
segundo_caracter = mensagem[1] # 'y'
ultimo_caracter = mensagem[-1] # 'n' (último caracter da string)

# Exemplo de acesso a caracteres em uma string
mensagem = "Python"
primeiro_caracter = mensagem[0] # 'P'
segundo_caracter = mensagem[1] # 'y'
ultimo_caracter = mensagem[-1] # 'n' (último caracter da string)

# Exemplos de operações com strings
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome # Concatenação
mensagem_repetida = "Olá! " * 3 # Repetição
parte_do_nome = nome[0:2] # Fatiamento (slicing)

# Exemplos de funções e métodos para strings
texto = "Olá, mundo!"
tamanho = len(texto) # Retorna o tamanho da string
maiusculo = texto.upper() # Converte para letras maiúsculas
minusculo = texto.lower() # Converte para letras minúsculas
contagem = texto.count('o') # Conta a ocorrência de um caracter ou substring
substituida = texto.replace('mundo', 'Python') # Substitui parte da string por outra


# Exemplo de formatação de strings
nome = "Alice"
idade = 25
mensagem_formatada = "Olá, meu nome é {} e tenho {} anos.".format(nome,idade)