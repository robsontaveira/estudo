# -- Indexando String -- 

# atribuido uma string
s = 'Data Science Academy'

print(s)    # imprime toda a variável

print(s[0]) # imprime o elemento de indice 0
print(s[1]) # imprime o elemento de indice 1
print(s[2]) # imprime o elemento de indice 2
print(s[3]) # imprime o elemento de indice 3
print(s[4]) # imprime o elemento de indice 4
print(s[5]) # imprime o elemento de indice 5

# retorna todos os elementos da string, iniciando pela posição indicada até o fim da string
print(s[1:])

# retornar tudo até a posição 2
print(s[:3])    # neste caso o indice 3 é excluido

# escreve contando do ultimo elemento
print(s[-1])

# retorna tudo exceto a ultima letra
print(s[:-1])

#saltar a string de 2 em 2, 3 em 3, 4 em 4 ...
print(s[::2])   # salto de 2 em 2
print(s[::3])   # salto de 3 em 3
print(s[::4])   # salto de 4 em 4

# escreve a string totalmente ao contrario
print(s[::-1])  #pega o ultimo caracter e salta de um em um no sentido contrario

# -- Funções Built-in de String

# deixa maiusculo
print(s.upper())

# deixa minusculo
print(s.lower())

# separa os caracteres com espaço entre eles
print(s.split())

# dividir uma string por um elemento especifico, exemplo y
print(s.split('y'))

# deixa a primeira letra maiscula
print(s.capitalize())

# contar quantas vezes o caracter 'a' aparece
print(s.count('a'))

# verifica se a string é só de número
print(s.isalnum())

# verifica se a string é toda espaço
print(s.isspace())

# verifica se a string termina com a letra 'o'
print(s.endswith('o'))


