"""Dada uma lista de números inteiros, escreva uma função para encontrar o
segundo maior valor na lista."""

def segundoMaiorNumero(listaDeNumeros):
  
  if len(listaDeNumeros) == 1: #função primeiro verifica se a lista de entrada listaDeNumeros está vazia
    return listaDeNumeros[0]
  else:
    lista_ordenada = sorted(listaDeNumeros, reverse=True) #Ordena os números em ordem decrescente 
    return lista_ordenada[1]

listaDeNumeros = [1, 2, -3, 4, 5,-8,9]
print(f"Nossa lista de números :{listaDeNumeros}")
print(f"O segundo maior número é o:", segundoMaiorNumero(listaDeNumeros))