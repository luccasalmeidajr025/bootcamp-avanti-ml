# Exemplos de valores booleanos
verdadeiro = True
falso = False

#Os principais operadores lógicos são: and, or e not
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
resultado_or = valor1 or valor2
resultado_not = not valor1

# Exemplo de expressão condicional usando boolean
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo de função com retorno booleano
def e_par(numero):
    return numero % 2 == 0
resultado = e_par(5)
print(resultado) # Output: False