# adicionar uma variável uma lista de numeros de 0 a 9
lista_numero = [x for x in range(10)]
print(lista_numero)

# usando o condicional no List Comprehension
lista_numeros = [x for x in range(10) if x<5]
print(lista_numeros)
print('\n\n')

# *******************************************************************
# exemplo dois
lista_frutas = ['banana','melancia','manga','cereja']
print('lista de frutas original',lista_frutas,'\n')

# loop tradicional para buscar palavra com letra m
nova_lista = []
for x in lista_frutas:
    if 'm'in x:
        nova_lista.append(x)
print('lista com loop tradicional',nova_lista)
print('\n')

# list comprehension para buscar palavra com letra m
nova_lista1 = [x for x in lista_frutas if 'm' in x]
print('lista com list comprehension',nova_lista1)

# -- Dict Comprehension --

dict_alunos = {'Bob':68,'Zico':57,'Ana':93}
print('Dicionario original',dict_alunos,'\n')

dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_status,'\n')

dict_alunos_status = {k:('Aprovado' if v>70 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos_status)