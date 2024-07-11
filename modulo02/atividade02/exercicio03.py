"""Escreva uma função que receba duas listas e retorne outra lista com os
elementos que estão presentes em apenas uma das listas."""

def elementos_unicos(lista1, lista2):
 
  # A utização da estrutura Set permite armazena uma coleção de elementos únicos e não ordenados
  listaA = set(lista1)
  listaB = set(lista2)

  # Encontra  os elementos únicos, relacionado a diferenaça entre as listas
  diferencaEntreListas = listaA ^ listaB

  # Converte a diferença em uma lista e retorna
  return list(diferencaEntreListas)


listaA = [1, 2, 3, 4, 5,6,7,8,9,10]
listaB = [1,2,3,5,7,11,13]

listaDeNumeros = elementos_unicos(listaA, listaB)
print(f"Elementos únicos: {listaDeNumeros}")
