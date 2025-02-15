tabuada = 2
contador = 1
resultado = 0




while  tabuada <= 10:
    while contador <= 10:
        resultado = tabuada * contador
        print(tabuada," x ", contador, " = ", resultado)
        contador += 1
    print('\n')   
    print('*******"TABUDA EM EXECUÇÃO"*********')
    tabuada +=1
    contador = 1
    print('\n')
print('*******"FIM!!!"*********')