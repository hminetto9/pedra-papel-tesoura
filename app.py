import random

# Mãos em ASCII art
mao_pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

mao_papel = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

mao_tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Função para obter a mão em ASCII art
def get_mao_ascii(escolha):
    if escolha == 'pedra':
        return mao_pedra
    elif escolha == 'papel':
        return mao_papel
    elif escolha == 'tesoura':
        return mao_tesoura
    return ""

print('Vamos jogar pedra, papel e tesoura !')
opcoes = ['pedra', 'papel', 'tesoura']
escolha_cpu = random.choice(opcoes)

# Corrigido: .strip() para remover espaços e .lower() para padronizar a entrada
escolha_player = str(input('Escolha Pedra / Papel / Tesoura: ')).strip().lower()

print(f'\nO computador escolheu: {escolha_cpu}')
print(get_mao_ascii(escolha_cpu))

print(f'\nVocê escolheu: {escolha_player}')
print(get_mao_ascii(escolha_player))

# Lógica para determinar o vencedor
if escolha_player == escolha_cpu:
    print('Empate!')
elif (escolha_player == 'pedra' and escolha_cpu == 'tesoura') or \
     (escolha_player == 'papel' and escolha_cpu == 'pedra') or \
     (escolha_player == 'tesoura' and escolha_cpu == 'papel'):
    print('Você ganhou !!')
else:
    print('Você perdeu !!')
