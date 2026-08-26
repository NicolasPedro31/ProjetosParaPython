import pandas as pd
import os

# 1. Força o Python a entrar na pasta correta do script
pasta_do_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(pasta_do_script)

try:
    df_marcas = pd.read_csv('marcas-carros.csv', sep=';')
    df_modelos = pd.read_csv('modelos-carro.csv', sep=';')
except FileNotFoundError:
    print("\n❌ Erro: Arquivos CSV não encontrados na pasta.")
    print(f"📍 Pasta atual onde o Python buscou: {pasta_do_script}")
    exit()

# Padroniza os textos dos CSVs para letras minúsculas
df_marcas['NOME_BUSCA'] = df_marcas['NOME'].astype(str).str.strip().str.lower()
df_modelos['NOME_BUSCA'] = df_modelos['NOME'].astype(str).str.strip().str.lower()


# --- SUPER MOTOR NUMÉRICO MULTI-IDIOMAS (0 ATÉ 1000) ---
def gerar_super_base_numerica():
    base = {}
    
    pt_un = ["", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    pt_un_alt = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    pt_11_19 = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    pt_dez = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    pt_cent = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    en_un = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    en_11_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    en_dez = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Base do idioma Tâmil (0 até 50) mapeada diretamente
    base["பூஜ்யம்"] = 0.0
    tm_0_10 = ["", "ஒன்று", "இரண்டு", "மூன்று", "நான்கு", "ஐந்து", "ஆறு", "ஏழு", "எட்டு", "ஒன்பது", "பத்து"]
    for i, nome in enumerate(tm_0_10):
        if nome: base[nome] = float(i)
    
    tm_11_20 = ["பதினொன்று", "பன்னிரண்டு", "பதின்மூன்று", "பதினான்கு", "பதினைந்து", "பதினாறு", "பதினேழு", "பதினெட்டு", "பத்தொன்பது", "இருபது"]
    tm_21_30 = ["இருபத்தொன்று", "இருபத்திரண்டு", "இருபத்துமூன்று", "இருபத்துநான்கு", "இருபத்தைந்து", "இருபத்தாறு", "இருபத்தேழு", "இருபத்தெட்டு", "இருபத்தொன்பது", "முப்பது"]
    tm_31_40 = ["முப்பத்தொன்று", "முப்பத்திரண்டு", "முப்பத்துமூன்று", "முப்பத்துநான்கு", "முப்பத்தைந்து", "முப்பத்தாறு", "முப்பத்தேழு", "முப்பத்தெட்டு", "முப்பத்தொன்பது", "நாற்பது"]
    tm_41_50 = ["நாற்பத்தொன்று", "நாற்பத்திரண்டு", "நாற்பத்துமூன்று", "நாற்பத்துநான்கு", "நாற்பத்தைந்து", "நாற்பத்தாறு", "நாற்பத்தேழு", "நாற்பத்தெட்டு", "நாற்பத்தொன்பது", "ஐம்பது"]
    
    for i, nome in enumerate(tm_11_20): base[nome] = float(11 + i)
    for i, nome in enumerate(tm_21_30): base[nome] = float(21 + i)
    for i, nome in enumerate(tm_31_40): base[nome] = float(31 + i)
    for i, nome in enumerate(tm_41_50): base[nome] = float(41 + i)

    # CORREÇÃO DA LINHA 49: Vetor numérico dos algarismos romanos preenchido corretamente
    def int_para_romano(num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
        romano = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]): romano += syb[i]; num -= val[i]
            i += 1
        return romano

    # Gerador principal (Português, Inglês e Romanos até 1000)
    for n in range(1, 1001):
        c, d, u = n // 100, (n % 100) // 10, n % 10
        val_float = float(n)
        
        if n == 100: p1, p2 = "cem", "cem"
        elif n == 1000: p1, p2 = "mil", "mil"
        else:
            pt = []; pt_a = []
            if c > 0: pt.append(pt_cent[c]); pt_a.append(pt_cent[c])
            if d == 1: pt.append(pt_11_19[u]); pt_a.append(pt_11_19[u])
            else:
                if d > 1: pt.append(pt_dez[d]); pt_a.append(pt_dez[d])
                if u > 0: pt.append(pt_un[u]); pt_a.append(pt_un_alt[u])
            p1, p2 = " e ".join(pt), " e ".join(pt_a)
        base[p1] = base[p2] = val_float
        
        if n == 1000: base["one thousand"] = val_float
        else:
            en = []
            if c > 0: en.append(f"{en_un[c]} hundred")
            r = n % 100
            if r > 0:
                if c > 0: en.append("and")
                if r < 10: en.append(en_un[r])
                elif 10 <= r < 20: en.append(en_11_19[r - 10])
                else:
                    if u > 0: en.append(f"{en_dez[d]}-{en_un[u]}"); base[f"{en_dez[d]} {en_un[u]}"] = val_float
                    else: en.append(en_dez[d])
            base[" ".join(en)] = val_float

        base[int_para_romano(n)] = val_float
        
    return base

# Inicializa o dicionário global na memória
DICIONARIO_NUMERICO = gerar_super_base_numerica()

def converter_texto_para_numero(entrada):
    texto_limpo = str(entrada).strip().lower()
    if texto_limpo in DICIONARIO_NUMERICO:
        return DICIONARIO_NUMERICO[texto_limpo]
    return float(entrada)


# --- INTERFACE DO USUÁRIO ---
print("=" * 45)
print("       SISTEMA DE LOCAÇÃO DE VEÍCULOS     ")
print("=" * 45)

while True:
    print("Marcas cadastradas no sistema:")
    marcas_disponiveis = df_marcas['NOME'].unique()
    print(", ".join(marcas_disponiveis))
    print("-" * 45)

    marca_usuario = input("Escolha e digite a marca desejada: ").strip().lower()
    busca_marca = df_marcas[df_marcas['NOME_BUSCA'] == marca_usuario]

    if busca_marca.empty:
        print(f"\n❌ Erro: A marca '{marca_usuario.upper()}' não existe no sistema. Tente novamente.\n")
        continue

    id_marca_encontrada = busca_marca.iloc[0]['ID']
    marca_formatada = busca_marca.iloc[0]['NOME']
    
    print(f"\nModelos disponíveis para a marca {marca_formatada}:")
    modelos_da_marca = df_modelos[df_modelos['IDMARCA'] == id_marca_encontrada]['NOME'].unique()
    print(", ".join(modelos_da_marca))
    print("-" * 45)
    
    modelo_usuario = input("Escolha e digite o modelo desejado: ").strip().lower()
    busca_modelo = df_modelos[
        (df_modelos['NOME_BUSCA'] == modelo_usuario) & 
        (df_modelos['IDMARCA'] == id_marca_encontrada)
    ]
    
    if busca_modelo.empty:
        print(f"\n❌ Erro: O modelo '{modelo_usuario.upper()}' não está disponível para a {marca_formatada}. Recomeçando...\n")
        continue
        
    modelo_formatado = busca_modelo.iloc[0]['NOME']
    print(f"\n✅ Veículo localizado: {marca_formatada} {modelo_formatado}")
    break

print("-" * 45)

while True:
    try:
        ano_usuario = int(input("Digite o ano do veículo (Ex: 2015): ").strip())
        if ano_usuario < 1900 or ano_usuario > 2027:
            print("❌ Erro: Por favor, digite um ano realista válido.")
            continue
        break
    except ValueError:
        print("❌ Erro: Digite o ano apenas com números numéricos.")

# --- LISTAS DE CATEGORIAS ---
populares = ["uno", "gol", "celta", "palio", "ka", "qq", "mobi", "argo"]
suvs_normais = ["tracker", "ecosport", "tucson", "captiva", "blazer", "duster", "s10", "ranger"]
marcas_luxo = ["mclaren", "ferrari", "bugatti", "lamborghini", "bentley", "aston martin", "porsche"]
modelos_esportivos = ["camaro", "corvette", "mustang", "r8", "gallardo", "murcielago"]

# Mapeamento dinâmico que avalia tanto a Marca quanto o Modelo digitado
if marca_usuario in marcas_luxo or modelo_usuario in modelos_esportivos:
    categoria, preco_diaria, preco_km = "Esportivo/Luxo", 250.00, 0.80
elif modelo_usuario in populares:
    categoria, preco_diaria, preco_km = "Popular", 50.00, 0.10
elif modelo_usuario in suvs_normais:
    categoria, preco_diaria, preco_km = "SUV/Normal", 120.00, 0.30
else:
    categoria, preco_diaria, preco_km = "Comum/Padrão", 80.00, 0.15

# --- VARIAÇÃO POR ANO ---
multiplicador_ano = 1.0
if ano_usuario >= 2020:
    multiplicador_ano = 1.20
    status_ano = "Novo (+20% Taxa)"
elif ano_usuario < 2010:
    multiplicador_ano = 0.85
    status_ano = "Antigo (-15% Desconto)"
else:
    status_ano = "Regular (Preço Padrão)"

preco_diaria *= multiplicador_ano
preco_km *= multiplicador_ano

print(f"\n📋 Categoria identificada: {categoria}")
print(f"📅 Ano informado: {ano_usuario} ↳ {status_ano}")
print(f"   ↳ Valor recalculado da diária: R$ {preco_diaria:.2f}")
print(f"   ↳ Valor recalculado por KM: R$ {preco_km:.2f}")
print("-" * 45)

while True:
    try:
        entrada_dias = input("Quantos dias alugado: ")
        dias = converter_texto_para_numero(entrada_dias)
        if dias < 0 or dias > 1000: raise ValueError
        break
    except ValueError:
        print("❌ Erro: Entrada inválida. Digite de 0 a 1000.")

while True:
    try:
        entrada_km = input("Quantos KM rodados: ")
        km = converter_texto_para_numero(entrada_km)
        if km < 0 or km > 1000: raise ValueError
        break
    except ValueError:
        print("❌ Erro: Entrada inválida. Digite de 0 a 1000.")

# Cálculo final baseado em todas as regras agregadas
pago = (dias * preco_diaria) + (km * preco_km)

print("-" * 45)
print(f"💰 O total a pagar é de: R$ {pago:.2f}")
print("=" * 45)