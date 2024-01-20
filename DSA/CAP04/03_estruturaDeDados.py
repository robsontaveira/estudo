# -- Listas --

# lista pode ter números e string
lista = [1, 2, 'nome']
print(lista,'\n')

# atribuir cada valor da lista a uma variável diferente
item1 = lista[0]
item2 = lista[1]
item3 = lista[2]
print(item1, item2, item3,'\n')

# mudando elemento da lista, exemplo mudar o elemento de indice [1]
lista[1] = 'oi'
print(lista,'\n')

# deletar um elemento da lista
del lista[0]
print(lista,'\n')

# Lista Aninhada
lista_1 =[[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print(lista_1,'\n')

# atribuindo um item da lista a uma variavel
a = lista_1[0]
print(a,'\n')

# atribuindo um item da variável a na variável b
b = a[0]
print(b,'\n')

# outra maneira de fazer os ultimos dois passos
c = lista_1[0][0]
d = lista_1[1][0]
print(c,'\n')
print(d,'\n')

# concatenar listas
lista_2 = [10,20]
lista_3 = [5,9]
lista_2e3 = lista_2 + lista_3
print(lista_2e3,'\n')


# Funções Built-in para listas
listaNum = [10,20,50,-3,4]

# função len() retorna o comprimento da lista
print(len(listaNum))

# função max() retorna o valor máximo da lista
print(max(listaNum))

# função min() retorna o valor mínimo da lista
print(min(listaNum))

# adicionar um item a lista
print(listaNum)     # antes de add
listaNum.append(11) # add 11 na lista
print(listaNum)     # depois de add

# passar elemento de uma lista para outra lista
old_list = [1,2,5,10]
new_list = []
for item in old_list:
    new_list.append(item)
print(new_list)

# saber o indice de um elemento da lista
print(listaNum.index(20))   # 20 esta no indice 1 da lista

# inserir um elemento na lista em um indice determinado
listaNum.insert(2,110)
print(listaNum)

# remover elemento da lista
listaNum.remove(110)
print(listaNum)

# -- Dicionários --

estudantes = {'Ana':22,'Ronaldo':26,'Janaina':25}

# saber a idade de Ana
print(estudantes['Ana'])

# adicionar dados ao dicionario
print(estudantes)
estudantes['João']=36
print(estudantes)

# retornar somente as chaves do dicionário
print('As chaves do dicionário são: ',estudantes.keys())

# retornar somente os valores do dicionário
print('Os valores do dicionário são: ',estudantes.values())

# retornar somente os elemntos do dicionário
print('Os elementos do dicionário são: ',estudantes.items())

# adicionar outro dicionario ao primeiro
estudantes1 = {'Isa':27,'Adriana':28}
estudantes.update(estudantes1)
print(estudantes)

# saber o tamanho do dicionário
tamanaho = len(estudantes)
print('O dicionário tem ',tamanaho,' elementos')

# limpar dados do dicionário
estudantes.clear()
print(estudantes,'\n')

# deletar um diconario
del estudantes

# criando dicionário com listas
dict = {'chave1':123,'chave2':[22,73.4],'chave3':['picanha','fraldinha','alcatara']}
print(dict)

# mostrando valor da chave2
print(dict['chave2'])

# mostrar um item da lista, dentro do dicionário, e escrevendo com letra maiuscula
print(dict['chave3'][0].upper())

# operações com items da lista, dentro do dicionário
var1 = dict['chave2'][1]-3
print(var1)

# duas operações no mesmo comando, para atualizar um item dentro da lista
print(dict['chave2'])
dict['chave2'][0]-=2
print(dict['chave2'])


# -- Tuplas --

tupla = ('Georgrafia',23,9.8)
print(tupla)

# vendo o tamanho de uma tupla
print(len(tupla))

# vendo elemento especifico da tupla
print(tupla[0])

# ver posição de um elemento da tupla
print(tupla.index(23))

# slicing com tupla
print(tupla[1:])

# usando função list() para converter uma tupla para lista
lista_tupla = list(tupla)
print(type(list_tupla))

# usando a funão tuple() ára converter uma ista para tupla
tupla2 = tuple(lista_tupla)
print(type(tupla2))
