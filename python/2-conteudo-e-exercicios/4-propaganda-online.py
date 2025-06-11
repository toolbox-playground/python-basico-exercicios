# Na lista propaganda_online abaixo, estão presente os dados de usuários que acessaram um determinado site e se o mesmo clicou em uma propaganda.

propaganda_online = [
  {'tempo_gasto_site': 68.95, 'idade': 35, 'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh', 'pais': 'Tunisia', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 80.23, 'idade': 31, 'tempo_gasto_internet': 143.77, 'cidade': 'West Jodi', 'pais': 'Nauru', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 69.47, 'idade': 26, 'tempo_gasto_internet': 236.50, 'cidade': 'Davidton', 'pais': 'San Marino', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 68.37, 'idade': 35, 'tempo_gasto_internet': 125.58, 'cidade': 'South Manuel', 'pais': 'Iceland', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 88.91, 'idade': 33, 'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad', 'pais': 'Myanmar', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 65.12, 'idade': 48, 'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury', 'pais': 'Australia', 'clicou_no_ad': 1},
  {'tempo_gasto_site': 74.53, 'idade': 30, 'tempo_gasto_internet': 221.51, 'cidade': 'West Colin', 'pais': 'Grenada', 'clicou_no_ad': 1},
  {'tempo_gasto_site': 69.88, 'idade': 20, 'tempo_gasto_internet': 123.82, 'cidade': 'Ramirezton', 'pais': 'Ghana', 'clicou_no_ad': 0}
]

# 1. Imprima os valores idade

for dado in propaganda_online:
    print(dado['idade'])

# 2. # 1. Imprime os valores tempo_gasto_site

for dado in propaganda_online:
  print(dado['tempo_gasto_site'])


# 3. Utilize a estrutura if/else juntamente com o for para imprimir a cidade dos usuários que gastaram mais de 150 horas de tempo na internet

for dado in propaganda_online:
    if dado['tempo_gasto_internet'] > 150:
      print(dado['cidade'])

# 4. Imprima o país dos usuários que clicaram na propaganda

for dado in propaganda_online:
   if dado['clicou_no_ad'] == 1:
      print(dado['pais'])

# 5. Imprima o páis e a cidade dos usuários com idade acima ou igual a 30 anos que gastaram mais de 70 minutos no site

for dado in propaganda_online:
   if dado['idade'] >= 30 and dado['tempo_gasto_site'] > 70:
      print(dado['pais'], dado['cidade'])
