""" Escreva uma função que receba uma lista de números e retorne outra lista
com os números ímpares."""


def listaDeImpares(listaDeNumeros):
   
    lista_impares = []  # Lista para armazenar números ímpares
    for numero in listaDeNumeros:
        if numero % 2 != 0:  # Verifica se o número é ímpar
            lista_impares.append(numero)  # Adiciona o número ímpar a lista
    return lista_impares

listaDeNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_impares = listaDeImpares(listaDeNumeros)
print(f"Nossa lista de números :{listaDeNumeros}")
print(f"Lista de números ímpares: {lista_impares}")