# 1. Verificar se a pessoa é maior de idade

# Insira sua idade
idade = int(input("Digite sua idade: "))

# Verifica se a idade é menor, maior ou igual a 18
if idade > 18:
    print("Você é maior de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é menor de idade.")



# 2. Verifica se o número é par ou ímpar e maior que 10
 
# Inserir um número
numero = int(input("Digite um número: "))

# Verifica se o número é par
if numero % 2 == 0:
    print("O número é par")
else:
    # Se o número é ímpar, verifica se está entre 1 e 10
    if 1 <= numero < 10:
        print("O número é ímpar e menor que 10")
    else:
        print("O número é ímpar e maior que 10")