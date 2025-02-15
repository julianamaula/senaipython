'''nota = float(input('Digite uma nota entre 0 e 10: '))

if nota > 5:
    print('Você foi aprovado! ')
elif nota > 3:
    print('Você está de Recuperação! ')
else:
    print('Você Reprovou! ')'''



'''Exemplo diferente do nº 1'''

nota = float(input('Digite uma nota: '))

if nota > 10:
    print('Você digitou número inválido! ')
else: 
    print('Você não digitou maior que 10! ')


if nota >= 5:
    print('Aprovado! ')
else:
    print('Você não digitou maior/igual que 5! ')


if nota >= 3:
    print('Recuperação')
else:
    print('Você não digitou maior/igual que 3! ')


if nota < 0:
    print('Você digitou número inválido! ')
else:
    print('Você não digitou menor que 0 - e está Reprovada! ')
                    


