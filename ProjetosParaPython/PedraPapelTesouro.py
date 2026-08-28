from enum import Enum

nome1 = input('digite seu nome: \n')
nome2 = input('digite seu nome: \n')

user1 = input('\n-----BEM VINDO-----\n-----PEDRA< PAPEL E TESOURA-----\nfaça sua escolha(pedra, papel e tesoura)\n')
user2 = input('\nfaça sua escolha:(pedra, papel e tesoura)\n')

# class jogo(str, Enum):
#     papel = ('papel', 'Papel', 'PAPEL')
#     pedra = ('pedra', 'Pedra', 'PEDRA')
#     tesoura = ('tesoura', 'Tesoura', 'TESOURA')

# if user1 == jogo.papel and user2 == jogo.pedra:
#     print(f'parabéns {nome1}, você venceu o {user2}')

user1=user1.strip()
user1=user1.lower()


user2=user2.strip()
user2=user2.lower()

if user2 == 'pedra' and user1 == 'papel':
    print(f'Parabéns {nome1}, você venceu o {nome2}!!!')
elif user1 == 'pedra' and user2 == 'papel':
    print(f'Parabéns {nome2}, você venceu o {nome1}!!!')
elif user1 == 'papel' and user2 == 'papel':
    print(f'Parabéns {nome1}, {nome2} vocês empataram!!!')
elif user1 == 'pedra' and user2 == 'pedra':
    print(f'Parabéns {nome1}, {nome2} vocês empataram!!!')
elif user1 == 'tesoura' and user2 == 'tesoura':
    print(f'Parabéns {nome1}, {nome2} vocês empataram!!!')
elif user1 == 'pedra' and user2 == 'tesoura':
    print(f'Parabén {nome1}, você venceu o {nome2}!!!')
elif user2 == 'pedra' and user1 == 'tesoura':
    print(f'Parabén {nome2}, você venceu o {nome1}!!!')
elif user1 == 'tesoura' and user2 == 'papel':
    print(f'Parabén {nome1}, você venceu o {user2}')
elif user2 == 'tesoura' and user1 == 'papel':
    print(f'Parabén {nome2}, você venceu o {user1}')
else:
    print('jogadadas invalidas')