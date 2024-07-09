#Loop for - Sintaxe
for elemento in sequencia: # type: ignore
# Código a ser executado para cada elemento

# Exemplo de loop "for" com lista
    frutas = ['maçã', 'banana', 'laranja']
    for fruta in frutas:
        print(fruta)

# Exemplo de loop "for" com string
    texto = 'Python'
    for letra in texto:
        print(letra)

# Exemplo de loop "for" com intervalo numérico
    for numero in range(1, 6):
        print(numero)

# Exemplo de loop "for" com intervalo numérico e passo
    for numero in range(1, 11, 2):
        print(numero)
# Exemplo de loop "for" com lista de tuplas
    pessoas = [('João', 25), ('Maria', 30), ('Pedro', 22)]
    for nome, idade in pessoas:
        print(f"{nome} tem {idade} anos.")

# Exemplo de loop "for" com dicionário
idades = {'João': 25, 'Maria': 30, 'Pedro': 22}
# Iteração sobre as chaves
for nome in idades:
    print(nome)
# Iteração sobre os valores
for idade in idades.values():
    print(idade)


# Exemplo de loop "for" com dicionário
idades = {'João': 25, 'Maria': 30, 'Pedro': 22}
# Iteração sobre as chaves
for nome in idades:
    print(nome)
# Iteração sobre os valores
for idade in idades.values():
    print(idade)

# Exemplo de uso de "enumerate()"
frutas = ['maçã', 'banana', 'laranja']
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

