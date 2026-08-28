import random

nome1 = input('qual seu nome amigo?')
nome2 = input('qual seu nome amigo?')



while True:
    n_secreto = random.randint(0,10)
    n1 = int(input('digite um numero de 0 até 10'))
    n2 = int(input('digite um numero de 0 até 10'))
    if n1 == n_secreto :
        print(f'você ganhou {nome1}')
        break
    elif n2 == n_secreto:
        print(f'você ganhou {nome2}')
        break