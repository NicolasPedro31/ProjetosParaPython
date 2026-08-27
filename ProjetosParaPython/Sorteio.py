import random
import repeat

nome = str(input("Coloque seu nome: ")) 
nome2 = str(input("Coloque seu nome: ")) 
nome3 = str(input("Coloque seu nome: ")) 

p1 = int(input("Digite um numero para ganhar: "))
p2 = int(input("Digite um numero para ganhar: "))
p3 = int(input("Digite um numero para ganhar: "))

num = random.randint(1, 2)
if (p1) ==  (num): 
        print(f"Parabéns {nome}, você ganhou!")
else: print(f"Voce não ganhou: {nome}")

if (p2) ==  (num):
        print(f"Parabéns {nome2}, você ganhou!")
else: print(f"Voce não ganhou: {nome2}")

if (p3) ==  (num):
        print(f"Parabéns {nome3}, você ganhou!")
else: print(f"Voce não ganhou: {nome3}")
print(f'Esse foi o numero sorteado {num}!')


if p1 == num or p2 == num or p3 == num:
        print("Novo sorteio")
repeat = num = random.randint(1, 2)
if p1 == num| p2 == num| p3 == num:
        print(f"Você ganhou {p1}, {p2}, {p3}")