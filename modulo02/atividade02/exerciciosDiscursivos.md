# Questões dissertativas sobre python

6. **Observe os espaços sublinhados e complete o código.**

import ___**matplotlib**.pyplot as plt
import numpy as _**np**__
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
layout="constrained")
for _**row**__ in range(2):
for _**col**__ in range(2):
axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
transform=axs[row, col].transAxes,
ha='center', va='center', __**fontsize**_=18,
color='darkgrey')
fig.suptitle('_**plt**.subplots()')

7. **Observe os espaços sublinhados e complete o código.**

import numpy as np
import __**matplotlib**________ as mpl
import __**matplotlib.pyplot**______ as plt
x = np._**linspace**_______(-2 * np.pi, 2 * np.pi, 100)
y = np._**sin**___(x)
_**fig**_, _**ax**_ = plt.subplots()
ax.**plot**____(**x_, y**_)

8. **Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?**

*O primeiro passo é importar a biblioteca pandas:*

>>> import pandas as pd

*o Segundo passo é a leitura do arquivo CSV em um DataFrame usando a função read_csv()*

>>> df = pd.read_csv("meu_arquivo.csv")

*Para visualizar as  primeiras linhas basta usar a função head(), se necessário é possível especificar o tamanho por passando por pârametro*

>>> print(df.head(10))

9. **Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?**

*É possível obter este resultando utilizando colchetes ou query. Após realizar a importação da biblioteca panda e a leitura do arquivo como mencionado na questão anterior, será necessário obter por uma dessas alternativas e seguir a sintaxe abaixo.*

**Usando colchetes**

>>> df["Idade"][df["Idade"] > 18]
*basta especificar a coluna e a condição dentro dos colchetes.*

**Usando query**

>>> df.query("SELECT Idade WHERE Idade > 18")
*possibilita realizar consultas complexas com sintaxe similar ao SQL*

10. **Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?**

*O primeiro passo para resolver essa situação é a Llocalizando os valores ausentes usando so métodos
isnull(): Verifica se um valor é NaN,sum(): Conta os NaNs em cada coluna ou describe(): Mostra a contagem de NaNs por coluna. A utlização destes métodos deve seguir a sintaxe abaixo:*

>>> df["Salário"].isnull()
>>> df.isnull().sum()
>>> df.describe(include='all')

*Em seguida, vamos analisar a quantidade e decidir a melhor solução. Que pode ser excluir usando o método dropna(). Exemplo:*

>>> df.dropna(subset=['idade', 'País'])

*Ou, Preencha com um valor (média, mediana, etc.) ou utilize interpolação. Exemplo:*
>>> df['Preço'].fillna(df['Preço'].mean(), inplace=True)

