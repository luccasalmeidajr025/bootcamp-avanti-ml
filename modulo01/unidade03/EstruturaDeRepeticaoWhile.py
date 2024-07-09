#Loop While - Sintaxe

while condicao:
# Código a ser executado enquanto a condição for verdadeira

# Exemplo de loop "while"
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1   

# Exemplo de loop "while" com "break"
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break   

# Exemplo de loop "while" com "continue"
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue # Pula a iteração quando contador == 3
print(contador)     

# Exemplo de loop "while" para iterar sobre lista
frutas = ['maçã', 'banana', 'laranja']
indice = 0
while indice < len(frutas):
    print(frutas[indice])
    indice += 1

# Exemplo: Criando uma lista de números pares. Função range()
numeros_pares = list(range(2, 11, 2))
print(numeros_pares)
# Saída: [2, 4, 6, 8, 10]