#------Manipulação de dados 1/5-----

#Abrindo o Arquivo para leitura
arq1 = open('teste.txt','r')#r => read

#lendo arquivo
print('\n',arq1.read())

#contar o numero de caracteres
print(arq1.tell(),'\n')

#retorna o cursor para o inicio do arquivo
arq1.seek(0,0)

#ler arquivo ate o caracter 12
print('\n',arq1.read(12),'\n')

print(arq1.read())

#------Manipulação de dados 2/5-----

#Abrir arquivo para gravação
arq2 = open('teste1.txt','w')#w => write

#Mudar o arq2
arq2.write('Aprenda a programar na linguagem python')
arq2.close()

#Acrescentar conteudo em arq2
arq2 = open('teste1.txt','a')#a => append
arq2.write('. Aprendendo python com DSA')
arq2.close()

#------Manipulação de dados 3/5-----
#------Manipulação de dados 4/5-----
#------Manipulação de dados 5/5-----

#usando pandas para leitura de arquivo
#import pandas as pd

import pandas as pd
arquivo = "salarios.csv"
df = pd.read_csv(arquivo)
#df.head()
print(df)

print('Fim do codigo')
