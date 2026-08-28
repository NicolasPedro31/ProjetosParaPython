import random
import time
import sys

def efeito_digitacao(texto, velocidade=0.03):
    """Gera um efeito visual de digitação no terminal."""
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def realizar_suspense(mensagem, segundos=3):
    """Cria um efeito de carregamento visual para dar suspense."""
    sys.stdout.write(mensagem)
    for _ in range(segundos):
        time.sleep(0.6)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n")

# 1. Configuração inicial dos dados
lideres = ["Bruna", "Nicolas", "Giovana", "Emanu", "Julia"]
fixos_nicolas = ["Nicolas Lopes", "Maycon", "Raquel", "Karina", "Vitor diogo"]

participantes_restantes = [
    "Ana Luiza", "Beatriz", "Davi", "José", "Livia", 
    "Marcos", "Manuela", "Nicole", "Caio", "Raissa", 
    "Rafaela", "Sophia", "Vitor hugo", "Rian"
]

# Inicializa as listas dos grupos
grupos = {lider: [] for lider in lideres}
grupos["Nicolas"] = fixos_nicolas
lideres_restantes = ["Bruna", "Giovana", "Emanu", "Julia"]

# Realiza o sorteio nos bastidores
random.shuffle(participantes_restantes)
for i, participante in enumerate(participantes_restantes):
    lider_atual = lideres_restantes[i % len(lideres_restantes)]
    grupos[lider_atual].append(participante)

# =====================================================================
# INÍCIO DA APRESENTAÇÃO SHOW DO SORTEIO
# =====================================================================
print("\n" + "="*50)
efeito_digitacao("🎉 BEM-VINDOS AO SUPER SORTEIO DE GRUPOS! 🎉", 0.05)
print("="*50 + "\n")
time.sleep(1)

# Contagem Regressiva Geral
print("O sorteio começará em...")
for i in range(3, 0, -1):
    print(f"⏱️  {i}...")
    time.sleep(1)
print("\n🚀 VALENDO! 🚀\n")
time.sleep(0.5)

# Apresentação do Grupo do Nicolas (Corrigido aqui!)
efeito_digitacao("📢 Primeiro grupo: Definido previamente por critérios técnicos!")
realizar_suspense("Montando a equipe do líder **Nicolas**")
print(f"👥 Grupo do Nicolas ({len(grupos['Nicolas'])} pessoas):")
for membro in grupos["Nicolas"]:
    time.sleep(0.4)
    print(f"  ⭐ {membro}")
print("-" * 40 + "\n")
time.sleep(1.5)

# Sorteio dos demais grupos com suspense de tempo
efeito_digitacao("🎲 Agora, iniciaremos o sorteio aleatório para os demais líderes!")
time.sleep(1)

for lider in lideres_restantes:
    realizar_suspense(f"Sorteando os integrantes para o grupo da/do **{lider}**")
    
    print(f"👥 Grupo da/do {lider} ({len(grupos[lider])} pessoas):")
    for membro in grupos[lider]:
        time.sleep(0.6)  # Pausa dramática para revelar cada pessoa do grupo
        print(f"  👤 {membro}")
    
    print("-" * 40 + "\n")
    time.sleep(1.5)  # Pausa antes de passar para o próximo líder

# Encerramento da apresentação
print("="*50)
efeito_digitacao("✨ Sorteio concluído com sucesso! Boa sorte aos grupos! ✨", 0.05)
print("="*50 + "\n")