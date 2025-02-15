# Intruções:

# 1. Definir a variável da tabuada.
# 2. Definir uma variável de contador.
# 3. Criar um loop.
# 4. Multiplicar as variaáveis e aguardar o resultado.
# 5. Mostrar o resultado.
# 6. Somar 1 ao valor do contador.

# Criando a variável e contador:

tabuada = 2
contador = 1
resultado = 0

# Criando uma condição:

while  tabuada <= 10:
    resultado = tabuada * contador
    print(tabuada," x ", contador, " = ", resultado)
    contador += 1
    if  contador >= 10:
        tabuada+=1
        contador=1
  
    





'''numerador = int(input("Qual número que quer que faça a tabuada: "))
print("\n")
for i in range(1,11):
    r = i * numerador
    print("{} x {} = {}".format(numerador,i,r))
    i = i + 1'''
