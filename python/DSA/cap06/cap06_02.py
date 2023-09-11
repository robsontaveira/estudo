#Manipulando arquivo TXT com pacote OS

texto = 'Cientista de dados pode ser uma otima alternativa de carreira.\n'
texto = texto + 'Esses profissionais precisão saber como programar em python\n'
texto += 'E, claro, devem ser proeficientes em Data Science'
print(texto)

#importando pacote OS
import os
#criando um arquivo
arquivo = open(os.path.join('cientista.txt'),'w')
#gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')
#fechando arquivo
arquivo.close()

#Manipulando arquivos TXT com expressão WITH
with open('cientista.txt','r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))
print(conteudo)

#usando para gravar texto
with open('cientista.txt','w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[19:])

#Manipulando arquivos CSV - Comma-Separated Values
import csv      #importando o módulo csv
with open('numeros.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('nota1','nota2','nota3'))
    writer.writerow((63,87,92))
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

#Leitura de arquivos CSV
with open('numeros.csv','r',encoding='utf8',newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

#criando uma lista com arquivo csv
with open('numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
#imprimindo a partir da segunda linha
for linha in dados[1:]:
    print(linha)

#Manipulando Arquivos JSON - JavaScript Object Notation
#criando um dicionário
dict_guido = {'nome':'Guido Van Rossum','linguagem':'python'}
#impriindo o dicionário criado
for k,v in dict_guido.items():
    print(k,v)
#importando o módulo JSON
import json
#convertendo o dicionário para um objeto json
json.dumps(dict_guido)
#criando um arquivo json
with open('dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict_guido))
#leitura de arquivo json
with open('dados.json','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
    
#Extração de Arquivo da Web
#Imprimindo um arquivo JSON copiado da internet
from urllib.request import urlopen

response = urlopen('http://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print('\nTitulo:',dados['title'])
print('URL:',dados['url'])
print('duração:',dados['duration'],'\n')

#Copiando o conteúdo de um arquivo para outro (2 métodos)
#Nome dos arquivos
arquivo_fonte = 'dados.json'
arquivo_destino = 'dados.txt'

#Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)

#Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())

#Leitura do arquivo txt
with open('dados.txt','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
print(dados)


