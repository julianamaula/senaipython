# Entrada criando uma calculadora:
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))

print('Qual operação você deseja? Digite: ')
print('A - Adição')
print('S - Subtração')
print('M - Multiplicação')
print('D - Divisão')
print('P - Potência')

operacao = input('Qual sua escolha? ')



# Processamento
resultado = 0

# usando upper -> converte o conteúdo da variável que foi digitada em letra maiscúla
# usando lower -> converte o conteúdo da variável que foi digitada em letra minúscula 
if (operacao.upper() == 'A'):
    resultado = numero1 + numero2
elif (operacao.upper() == 'S'):
    resultado = numero1 - numero2
elif (operacao.upper() == 'M'):
    resultado = numero1 * numero2
elif (operacao.upper() == 'D'):
    resultado = numero1 / numero2
elif (operacao.upper() == 'P'):
    resultado = numero1 ** numero2
else:
     resultado = 'Opção inválida'
    


#Saida
print('O resultado é: ' , resultado)