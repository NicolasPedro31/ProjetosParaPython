import pandas as pd

nome = input("Digite seu nome completo: ")
dia = input("Digite o dia do seu aniversário: ")
mes = input("Digite o seu mês: ")
ano = input("Digite o seu ano: ")
senha = input("Digite sua senha: ")
dados = {
    "Campo": ["Nome completo", "Dia", "Mês", "Ano", "Senha"],
    "Valor": [nome, dia, mes, ano, "*" * len(senha)],
}

Tabela = pd.DataFrame(dados)

print("\n--- Dados Cadastrados em Tabela ---")
print(Tabela.to_string(index=False))
print("\nObrigado, dados cadastrados!")