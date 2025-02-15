#comando While

senha = "abcd1234"
senhaCorreta = " "

# Primeiro modelo do primeiro exercíciofeito pelo Professor
while senhaCorreta != senha:# Enquanto a senha correta for diferente da senha
    senhaCorreta = input("Digite a senha correta: ")# Pedindo a senha
    if senhaCorreta != senha:# Se a senha estiver errada
        print("Senha inválida! ")# Mostrando que a senha está errada
print("Senha correta! ")# Mostrando que a senha está correta


# Segundo modelo do primeiro exercício
'''senhaCorreta = False
contador = 0  # Inicializando o contador
while not senhaCorreta:  # O loop continuará até que a senha seja correta
    print("Contando: ", contador)# Mostrando o contador
    contador += 1 # Incrementando o contador
    resposta = input("Digite a senha correta: ")# Pedindo a senha
    if resposta != "abcd1234":# Se a senha estiver errada
        senhaCorreta = False# A senha continua incorreta
    else:# Se a senha estiver correta
        senhaCorreta = True# A senha está correta
print("Senha correta!")# Mostrando que a senha está correta'''
