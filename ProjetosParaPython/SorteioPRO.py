import random

# Removido o import repeat pois ele não existe no Python

nome = str(input("Coloque seu nome: ")) 
nome2 = str(input("Coloque seu nome: ")) 
nome3 = str(input("Coloque seu nome: ")) 

p1 = int(input("Digite um numero para ganhar: "))
p2 = int(input("Digite um numero para ganhar: "))
p3 = int(input("Digite um numero para ganhar: "))

num = random.randint(1, 2)
print(f'\nEsse foi o numero sorteado inicial: {num}!')

# Variáveis para salvar quem acertou a primeira rodada
ganhou_p1 = (p1 == num)
ganhou_p2 = (p2 == num)
ganhou_p3 = (p3 == num)

# Exibe quem acertou e quem errou na primeira rodada
if ganhou_p1: print(f"Parabéns {nome}, você acertou!")
else: print(f"Você não ganhou: {nome}")

if ganhou_p2: print(f"Parabéns {nome2}, você acertou!")
else: print(f"Você não ganhou: {nome2}")

if ganhou_p3: print(f"Parabéns {nome3}, você acertou!")
else: print(f"Você não ganhou: {nome3}")

# --- INÍCIO DA LÓGICA DE DESEMPATE ---

# Cria uma lista apenas com os nomes de quem acertou
ganhadores = []
if ganhou_p1: ganhadores.append(nome)
if ganhou_p2: ganhadores.append(nome2)
if ganhou_p3: ganhadores.append(nome3)

# Se mais de uma pessoa acertou, começa o desempate
if len(ganhadores) > 1:
    print(f"\nTivemos um empate entre: {', '.join(ganhadores)}!")
    print("Iniciando o desempate até restar apenas UM vencedor...")
    
    while True:
        # Sorteia um novo número para a rodada de desempate
        num_desempate = random.randint(1, 2)
        print(f"\nNovo número sorteado para desempate: {num_desempate}")
        
        # Lista para armazenar quem acertou NESTA rodada de desempate
        acertaram_agora = []
        
        # Apenas quem estava no empate digita um novo palpite
        for jogador in ganhadores:
            palpite = int(input(f"Palpite de desempate para {jogador}: "))
            if palpite == num_desempate:
                acertaram_agora.append(jogador)
        
        # Verificamos o resultado da rodada de desempate:
        if len(acertaram_agora) == 1:
            # Se apenas UMA pessoa acertou, ela é a campeã final!
            print(f"\n🏆 FIM DE JOGO! O campeão final é: {acertaram_agora[0]}!")
            break  # Encerra o loop do desempate
            
        elif len(acertaram_agora) > 1:
            # Se duas ou mais pessoas continuam acertando, o loop repete com elas
            print(f"Continua o empate entre: {', '.join(acertaram_agora)}. Vamos de novo!")
            ganhadores = acertaram_agora  # Atualiza os finalistas
            
        else:
            # Se NINGUÉM acertou, todos os finalistas tentam de novo na próxima rodada
            print("Ninguém acertou nesta rodada de desempate. Tentem o mesmo número ou outro novamente!")