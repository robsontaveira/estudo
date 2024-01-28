# definindo a função
def primeiraFunc():
    print('Olá Mundo')

primeiraFunc()              # chamada da função

# definindo uma função com parâmetro
def segundaFunc(nome):
    print('Hello %s'%(nome))

segundaFunc('Aluno')        # chamada da função

# função para fazer a soma de dois números
def soma2num(num1,num2):
    print('Primeiro número é '+str(num1))
    print('Segundo número é '+str(num2))
    print('A soma é ',num1+num2)

soma2num(4,3)               # chamada de função

# função com número variável de argumentos
def printVarInfo(arg1,*vartuple):
    print('O parâmetro passado foi: ',arg1) # imprimindo o valor do argumento
    for item in vartuple:
        print('O parâmetro passado foi: ',item)
    return;

printVarInfo(10)


# -- scopo de variável - Local --

# variável global
var_global = 10
# função
def multiplica_numeros(num1,num2):
    var_global = num1*num2  # variável local
    print(var_global)

multiplica_numeros(5,5)
print(var_global)


# -- Expressão Lambda --

# definindo uma função em três linhas de código
def potencia (num):
    resultado = num**2
    return resultado

print(potencia(2))

# usando lambda
potenciaL = lambda num:num**2
potenciaL(5)