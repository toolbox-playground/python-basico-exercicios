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

# Saídas
1000
<class 'int'>
```

```python
juros = 0.05
tipo_juros = type(juros)

print(juros)
print(tipo_juros)

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

# Saída
1

# Saída
2
```

#### Exemplo: Total a pagar de um produto.

```py
preco = 0.25
quantidade = 47
total_a_pagar = quantidade * preco

print(total_a_pagar)

# Saída 
11.75
```

### Podemos ainda converter os tipos numéricos entre si utilizando o método nativo `int` e `float`:

```py
print(int(3.9))

# Saída
3
```

```py
print(float(10))

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

# Saída
True
```
```py
falso = False
print(falso)

# Saída
False
```
### São do tipo `bool`.

```py
print(type(True))

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

# Saída
True
```

#### Exemplo: Cartão de crédito

```py
codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

# Saída
False
```


# 2. Estruturas de Dados

### Estruturas de dados são fundamentais para armazenar e organizar dados em Python. As principais são:

- Listas (`list`)
- Tuplas (`tuple`)
- Dicionários (`dict`)
- Conjuntos (`set`)
  
## 2.1 Listas

### Armazenam sequências mutáveis e ordenadas de valores. Utilizamos `[]` e são do tipo `list`:

#### Exemplo: Login de Usuário

```py
usuario_web = ['Bruno Dela Val', 'bruno.delaval', 'bruno123', 'bruno.delaval@toolbox.com']

print(usuario_web)
print(type(usuario_web))

# Saída
['Bruno Dela Val', 'bruno.delaval', 'bruno123', 'bruno.delaval@toolbox.com']
<class 'list'>
```

#### Exemplo: Lista de Frutas
```py
# Criando uma lista
frutas = ["maçã", "banana", "laranja"]


# Acessando elementos
print(frutas[0])  # Saída: maçã


# Adicionando elementos
frutas.append("uva")
print(frutas)  # Saída: ['maçã', 'banana', 'laranja', 'uva']


# Removendo elementos
frutas.remove("banana")
print(frutas)  # Saída: ['maçã', 'laranja', 'uva']
```

### Podemos converter alguns tipos de variáveis em listas, como strings.
```py
nome = 'João'
caracteres_nome = list(nome)


print(nome) # Saída: João
print(caracteres_nome) # Saída: ['J', 'o', 'ã', 'o'] 
```

## 2.2 Tuplas 

### Tuplas são coleções ordenadas e imutáveis. Utilizamos `()` e são do tipo `tuple`:

Exemplo: Lista de Cores

```py
# Criando uma tupla
cores = ("vermelho", "verde", "azul")


# Acessando elementos
print(cores[1])  # Saída: verde
print(type(cores))  # Saída: <class 'tuple'>
```

### Tuplas são imutáveis, portanto não podemos adicionar ou remover elementos.

## 2.3 Dicionários

### Armazenam sequências no formato chave-valor. Utilizamos da seguinte forma (`{'chave': 'valor'}`) e são do tipo `dict`.

```py
brasil = {'capital': 'Brasília', 'idioma': 'Português', 'populacao': 210}

print(brasil.keys()) # Saída: dict_keys(['capital', 'idioma', 'populacao'])
print(brasil.values()) # Saída: dict_values(['Brasília', 'Português', 210])
```

#### Exemplo: Cadastro de Aluno
```py
# Criando um dicionário
aluno = {"nome": "Thiago", "idade": 25, "curso": "Engenharia"}


# Acessando valores
print(aluno["nome"])  # Saída: Thiago


# Adicionando um novo par chave-valor
aluno["nota"] = 90
print(aluno)  # Saída: {'nome': 'Thiago', 'idade': 25, 'curso': 'Engenharia', 'nota': 90}


# Removendo um par chave-valor
del aluno["idade"]
print(aluno)  # Saída: {'nome': 'Thiago', 'curso': 'Engenharia', 'nota': 90}
```

### Não permite chaves duplicadas.

#### Exemplo: Carro

```py
carro = {
    'marca': 'Volkswagen',
    'modelo': 'Polo',
    'ano': 2021,
    'ano': 2004
}

print(carro) # Saída: {'marca': 'Volkswagen', 'modelo': 'Polo', 'ano': 2004}
```

### Podemos criar dicionários compostos:

#### Exemplo: Cadastro

```py
cadastro = {
    'bruno': {
        'nome': 'Bruno',
        'ano_nascimento': 1900,
        'pais': {
            'pai': {
              'nome': '<nome-do-pai>',
              'ano_nascimento': 1971
            },
            'mae': {
              'nome': '<nome-da-mae>',
              'ano_nascimento': 1973
            },
        }
    }
}

print(cadastro['bruno']['pais']['mae']['ano_nascimento']) 

# Saída: 1973
```
## 2.4. Conjuntos

### Armazenam sequências imutáveis e desordenadas valores, sem repetição. São do tipo `set`:

```py
frutas = {'banana', 'maca', 'uva', 'uva'}

print(frutas) # Saída: {'maca', 'banana', 'uva'}
print(type(frutas)) # Saída: <class 'set'>
```

### Eles são úteis para operações matemáticas de diferença (`-`).

#### Exemplo: Países Diferentes

```py
norte_europa = {'reino unido', 'suecia', 'russia', 'noruega', 'dinamarca'}
escandinavia = {'noruega', 'dinamarca', 'suecia'}

norte_europa_nao_escandivano = norte_europa - escandinavia
print(norte_europa_nao_escandivano) 

# Saída: {'reino unido', 'russia'}
```

### Podemos converter conjuntos para lista e vice e versa.

#### Exemplo: Times Paulista

```py
times_paulistas = {'São Paulo', 'Palmeiras', 'Corinthians', 'Santos'}

print(times_paulistas) # Saída: {'Corinthians', 'São Paulo', 'Santos', 'Palmeiras'}
print(type(times_paulistas)) # Saída: <class 'set'>


print(list(times_paulistas)) # Saída: ['Corinthians', 'São Paulo', 'Santos', 'Palmeiras']
print(type(list(times_paulistas))) # Saída: <class 'list'>
```

# 3. Estrutura de Repetição

# 4. Condicionais

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



