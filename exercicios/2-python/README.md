# 1. Variáveis 

## 1.1 Numéricas

### As variáveis que armazenam valores numéricos podem ser de dois tipos:
- **Inteiros: `int`**
- **Decimais: `float`**

### Exemplo de Variáveis Numéricas

```python
preco = 1000
tipo_preco = type(preco)

print(preco)
print(tipo_preco)
```
```sh
# Saídas
1000
<class 'int'>
```

```python
juros = 0.05
tipo_juros = type(juros)

print(juros)
print(tipo_juros)
```

```sh
# Saídas
0.05
<class 'float'>
```


### A partir dos tipos numéricos podemos realizar as quatro operações matemáticas fundamentais:

 - Soma (`+`)
 - Subtração (`-`)
 - Multiplicação (`*`)
 - Divisão (`/`)

### Além de operações mais avançadas:

 - Divisão Inteira (`//`)
 - Exponenciação (`**`)
 - Resto de Divisão (`%`)

#### Exemplo: Carrinho de compra de um e-commerce.

```python
qtd_items_carrinho = 0

qtd_items_carrinho = qtd_items_carrinho + 1
print(qtd_items_carrinho)

qtd_items_carrinho = qtd_items_carrinho + 1
print(qtd_items_carrinho)
```

```sh
# Saída
1
```

```sh
# Saída
2
```

#### Exemplo: Total a pagar de um produto.

```py
preco = 0.25
quantidade = 47
total_a_pagar = quantidade * preco

print(total_a_pagar)
```

```sh
# Saída
11.75
```


### Podemos ainda converter os tipos numéricos entre si utilizando o método nativo `int` e `float`:

```py
print(int(3.9))
```

```sh
# Saída
3
```

```py
print(float(10))
```

```sh
# Saída
10.0
```

## 1.2 Strings

### Variáveis string do tipo `str` que armazenam texto. São definidas envolvendo o texto em aspas  simples (`'`) ou duplas (`"`).

#### Exemplos de string:

```py
# Definindo variáveis string
nome = "Maria"
mensagem = 'Olá, mundo!'

print(nome)  
print(mensagem)  
```
```sh
# Saídas
Maria
Olá, mundo!
```

### Variáveis do tipo string podem ser manipuladas utilizando a concatenação:

- Concatenação (`+`).

#### Exemplo: Nome completo.

```py
nome = 'Bruno'
sobrenome = 'Dela Val'

apresentacao = 'Olá, meu nome é ' + nome + ' ' + sobrenome + '.'
print(apresentacao)
```
```sh
# Saída
Olá, meu nome é Bruno Dela Val.
```

## 1.3 Boleanos

### Armazenam valores lógicos:

- Verdadeiro (`True`);
- Falso (`False`).

```py
verdadeiro = True
print(verdadeiro)
```
```sh
# Saída
True
```
```
falso = False
print(falso)
```
```sh
# Saída
False
```
### São do tipo `bool`.

```
print(type(True))
````
```sh
# Saída
<class 'bool'>
```

### São resultados de comparações lógicas. Os operadores de comparação lógica são:

- Maior (`>`);
- Menor (`<`);
- Igual (`==`);
- Maior ou Igual (`>=`);
- Menor ou Igual (`<=`);
- Diferente (`!=`).

#### Exemplo: Caixa eletrônico

```py
saldo_em_conta = 200
valor_do_saque = 100

executar_saque = valor_do_saque <= saldo_em_conta
print(executar_saque)
```

```sh
# Saída
True
```

#### Exemplo: Cartão de crédito

```py
codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)
```

```sh
# Saída
False
```

# 2. Estrutura de Repetição
# 3. Condicionais

### As estruturas condicionais controlam o fluxo de execução de um programa baseado em condições específicas. As principais estruturas ondicionais são:

  - `if`: Executa um bloco de código se a condição for verdadeira.
  - `elif`: Permite testar múltiplas condições.
  - `else`: Executa um bloco de código se nenhuma das condições anteriores for verdadeira.

### São descritos da seguinte maneira:

```py
if <booleano / comparação lógica> == True:
  <execute este código>
else:
  <senão execute este código>
```
#### Exemplo: Pessoa maior de idade.

```py
idade = 18

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")
```
### Também é possível aninhar condicionais para criar lógicas mais complexas:

```py
nota = 85
frequencia = 90

if nota >= 70:
    if frequencia >= 75:
        print("Você foi aprovado.")
    else:
        print("Reprovado por baixa frequência.")
else:
    print("Reprovado por nota insuficiente.")
```

### Outra possibilidade é utilizar operadores lógicos como `and`, `or`, e `not` para combinar múltiplas condições.

#### Exemplo: Vaga de emprego usando `and`:
```py
idade = 27
tem_diploma = True
experiencia_anos = 4

if idade >= 25 and tem_diploma and experiencia_anos >= 3:
    print("Você é elegível para a vaga de emprego.")
else:
    print("Você não é elegível para a vaga de emprego.")
```
#### Exemplo: Desconto para estudantes usando `or`:

```py
idade = 20
estudante = True

if idade < 18 or estudante:
    print("Você tem direito a um desconto.")
else:
    print("Você não tem direito a um desconto.")
```



