import random

print('Vamos jogar pedra, papel e tesoura !')

opcoes = ['pedra', 'papel', 'tesoura']
escolha_cpu = random.choice(opcoes)

escolha_player = str(input('Escolha Pedra / Papel / Tesoura: ')).lower()

print(f'O computador escolheu: {escolha_cpu}, e você escolheu: {escolha_player}')

if escolha_player == escolha_cpu:
    print('Empate!')
elif (escolha_player == 'pedra' and escolha_cpu == 'tesoura') or \
     (escolha_player == 'papel' and escolha_cpu == 'pedra') or \
     (escolha_player == 'tesoura' and escolha_cpu == 'papel'):
    print('Você ganhou !!')
else:
    print('Você perdeu !!')
