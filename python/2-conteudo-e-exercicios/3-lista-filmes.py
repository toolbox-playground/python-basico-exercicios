### LISTAS ###
  
# 1. Crie uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no site no IMDB. Imprima o resultado.

filmes = []

filmes.append('The Shawshank Redemption')
filmes.append('The Godfather')
filmes.append('The Dark Knight')
filmes.append('The Godfather Part II')
filmes.append('12 Angry Man')
filmes.append("Schindler's List")
filmes.append('The Lond of the Rings: The Return of the King')
filmes.append('Pulp Fiction')
filmes.append('The Lord of the Rings: The Fellowship of the Ring')
filmes.append('The Good, the Bad and the Ugly')

print(filmes)

# 1.1 Simule a movimentação do ranking. Utilize os métodos insert e pop para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.

filmes.insert(0, 'The Godfather')
filmes.insert(1, 'The Shawshank Redemption')

filmes.pop(2)
filmes.pop(2)

print(filmes)

### CONJUNTOS ###

# 2. Suponhamos que houve um erro no seu ranking. Simule a duplicação dos três últimos filmes da lista e imprima o resultado.

filmes.insert(7, 'Pulp Fiction')
filmes.insert(9, 'The Lord of the Rings: The Fellowship of the Ring')
filmes.insert(11, 'The Good, the Bad and the Ugly')

print(filmes)

# 2.1 Para remover os valores duplicados utilize a conversão set e list e imprima o resultado.

filmes = list(set(filmes))

print(type(filmes), len(filmes))
print(filmes)



### DICIONÁRIOS ###

# 3. Repita os exercícios da parte 1 (listas). Os elementos da lista filmes devem ser dicionários no seguinte formato: {'nome': <nome-do-filme>, 'ano': <ano do filme>}.

filmes = [
    {'nome': 'The Shawshank Redemption',
     'ano': 1994
     },

    {'nome': 'The Godfather',
     'ano': 1972
     },

     {'nome': 'The Dark Knight',
     'ano': 2008
     },

     {'nome': 'The Godfather Part II',
     'ano': 1974
     },

     {'nome': '12 Angry Men',
     'ano': 1957
     },

     {'nome': "Schindler's List",
     'ano': 1993
     },

     {'nome': 'The Lord of the Rings: The Return of the King',
     'ano': 2003
     },

     {'nome': 'Pulp Fiction',
     'ano': 1994
     },

     {'nome': 'The Lord of the Rings: The Fellowship of the Ring',
     'ano': 2001
     },

     {'nome': 'The Good, the Bad and the Ugly',
     'ano': 1966
     }

]

print(filmes)
