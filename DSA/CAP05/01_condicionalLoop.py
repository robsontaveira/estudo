# condicinal if
if 5>2:
    print('A sentença é verdade')

# condicional iff ... else
if 5<2:
    print('A sentença é verdadeira')
else:
    print('A sentença é falsa')

# condicional if ... else com variável
dia = 'terça'
if dia == 'segunda':
    print('Hoje fara sol')
else:
    print('Hoje vai chover')

# validar mais de uma condição usando if ... elif ... else
dia = 'quarta'
if dia == 'segunda':
    print('Hoje fará sol')
elif dia == 'terça':
    print('Hoje vai chover')
else:
    print('Sem previsão do tempo')


    # -- Loop For --

    # imprimir elementos de uma tupla
tp = (1,2,3)
for i in tp:
    print(i)

# imprimir os números no intervalo de 0-5
print('\nSegundo for')
for contador in range(0,5):
    print(contador)

# imprimindo os números pares de uma lista
print('\nImprimindo os números pares da lista')
lista = [1,2,3,4,5,6,7,8,9]
for num in lista:
    if (num%2) == 0:
        print(num)

# -- Loop For Aninhado --

lista1 = [0,1,2,3,4]
lista2 = [1,2,3]
# loop externo
for elemento_lista1 in lista1:
    # loop interno
    for elemento_lista2 in lista2:
        print('\n',elemento_lista1*elemento_lista2)
    print('----')

# exemplo 2
lista1 = [0,1,2,3,4]
lista2 = [1,2,3]
print('Lista 1: ',lista1)
print('Lista 2: ',lista2)
soma = 0
# loop externo
for lista in [lista1,lista2]:
    # loop interno
    for num in lista:
        # condicional
        if (num%2)==0:
            soma += num
print('A soma dos pares das listas é igual ',soma)


# -- Loop For em lista de listas (matrizes)

# loop para encontra maior numero em uma matriz
maior_numero = 0
matriz = [[42,23,34],[100,215,114],[10.1,98.7,12.3]]
# loop externo
for linha in matriz:
    # loop interno
    for num in linha:
        #condicional
        if num>maior_numero:
            maior_numero = num
print('O maior número é ',maior_numero)


# -- Loop While(enquanto)

# usando loop while para imprimir de 0-9
valor = 0
while valor<10:
    print(valor)
    valor = valor+ 1

# usar else para encerrar o loop while
print('\n')
x = 0
while x<10:
    print('O valor de x é ',x)
    print('x ainda é menor que 10, somando 1 a x')
    x += 1
else:
    print('Loop concluido')
print(x)


# -- Uasando Pass e Break com loop while

# se encontrarmos o número 4 interrompemos o loop
valor = 0
while valor < 10:
    if valor == 4:
        break
    else:
        pass
    print(valor)
    valor += 1

# -- Usando o continue com loop for

for letra in 'Python é zzz incrivel':
    if letra == 'z':
        continue
    print(letra)


# -- Loop While e For juntos

# Encontrar os números primos em uma coleção de números
# usando loop while e for juntos

lista_primo = []     # lista para receber os números primos
# loop  para percorer de 2-30
for num in range(2,31):
    primo = True    # variável de controle

    # loop while para verificar se o número é primo
    i = 2
    while i <= num//2:
        if num % i == 0:
            primo = False
            break
        i += 1
    # adiciona número primo na lista de primos
    if primo:
        lista_primo.append(num)
# imprimindo lista de números primos
print(lista_primo)