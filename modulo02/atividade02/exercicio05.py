"""Crie uma função que receba uma lista de tuplas, cada uma contendo o
nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
pessoas em ordem alfabética."""

def classificarNome(lista_tuplas):
  # Está função retira o nome de cada tupla
  def extrair_nome(tupla):
    return tupla[0]

  # Estabelece a ordem por nome
  return sorted(lista_tuplas, key=extrair_nome)


listaDeNomes = [("Carlos", 38), ("Paula", 22), ("José", 50), ("Aline", 19)]
listaOrdemAlfabetica = classificarNome(listaDeNomes)
print(f"Nossa lista de Nnomes :{listaDeNomes}")
print(listaOrdemAlfabetica)
