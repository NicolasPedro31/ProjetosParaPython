preco_original = float(input("Valor do produto: "))
porcentagem_aplicada = int(input("Valor do desconto: "))
novo = preco_original - (preco_original * porcentagem_aplicada / 100 )
print(f"O valor do desconto entre R${preco_original} e {porcentagem_aplicada}% é: {novo}: ")