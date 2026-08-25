# import pandas as pd

# linhas = []
# for i in range(1, 11):
#     for j in range(1, 11):
#         linhas.append({'X': i, 'Y': j, 'Resultado': i * j})

# tabela_longa = pd.DataFrame(linhas)

# tabuada_grade = tabela_longa.pivot(index='X', columns='Y', values='Resultado')

# print(tabuada_grade)
numero = int(input("\n------TABUADA------\nEscolha um numero"))
for i in range(1, 11):
    resultado = print(f"Seu resultado é:{numero * i}")
    
    