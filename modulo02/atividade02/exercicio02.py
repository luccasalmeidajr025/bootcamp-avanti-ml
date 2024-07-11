"""Escreva uma função que receba uma lista de números e retorne outra lista
com os números primos presentes."""

def numero_primo(numero): #Está função verifica se o número é primo
  for d in range(2, numero):
    if numero % d == 0:
      return False
  return True

primos = []
listaDeNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20] 
for i in listaDeNumeros: #condição para adicionar números primos em uma lista
    if numero_primo(i):
      primos.append(i)

print(f"Nossa lista de números :{listaDeNumeros}")
print(f"Lista de primos: {primos}") 