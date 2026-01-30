from operacoes.funcoes_matematicas import soma, subtracao, multiplicacao


# Dicionario

operacoes = {
    "1": (soma, "Soma"),
    "2": (subtracao, "Subtracao"),
    "3": (multiplicacao, "Multiplicação")
}

# Entrada

a = float(input("Escolha seu primeiro numero: "))
b = float(input("Escolha seu segundo numero: "))
print (" Escolha qual função você quer utilizar? ")
opcao = input("1 - Soma " \
"2 - Subtração " \
"3 - Multiplicação ")


# Verific Logic

dados = operacoes.get(opcao)

if dados:
    funcao, nome_da_op = dados
    resultado = funcao(a, b)
    operacao = nome_da_op
else:
    resultado = None
    print("Opção Inválida! ")

# saida
if resultado is not None:
    print (f"O resultado da {operacao} é: {resultado} ")
 
