limite = 101
contador = 0
sair = False # variável booleana é True ou False



'''primeiro exemplo Comando de repetição mostrando o contador
while contador >= limite:
    print("Contando: ", contador)
    contador = contador + 1
print("Final da contagem! ")'''



'''segundo exemplo mudando o tipo de contador exemplo Comando de repetição'''
while sair  == False:
    print("Contando: ", contador)
    contador  += 1
    resposta = input("Deseja parar o contador? S/N: ")
    if resposta == "N":
        sair = False
    else:
        sair = True
print("Final da contagem! ")
