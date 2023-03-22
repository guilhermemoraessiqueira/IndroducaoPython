'''
Comentário com 
várias linhas 
'''
# Texto e números
print("Idade: ", 41)

# Texto com booleano
print("Cerveja:", True)

# Textos longos, com mais de uma linha
print('''Cardapio:
    1 - Hamburguer
    2 - Pizza
    3 - Dogão
    4 - Refri ''')

print("--------------------------")

# Imprimir a mensagem 
#     "Professor, você é muito legal"
# Mas o muito deve ser repetido 25 vezes.
print("Prof, você é ", 25*"muito ", "legal")

print("--------------------------")

numero1 = 1
numero2 = 2
print("Numero {} é menor que o numero {}".format(numero1, numero2))

print("--------------------------")

pi =3.14
print(pi)

print("--------------------------")

ham=25
pizza=50
dogao=15
refri=10

print('''Cardapio:
    1 - Hamburguer {}
    2 - Pizza {}
    3 - Dogão {}
    4 - Refri {}'''.format(ham,pizza,dogao,refri))

print("--------------------------")

#Declarar a Variável tipo Lista
produtos = ['PS5', 'PS4', 'PS3']
precos =[4800,2500,1200]
#Imprimir as variáveis na tela (usar .format)
print("{}: {}".format(produtos, precos))

print("--------------------------")

#dicionário
dic ={
    "Nome do usuário": 'Guilherme Moraes',
    'login': 'moras.gui',
    'senha': 321,
    'email': 'guimora--essiqueira@gui.com'
}

print(dic)

print("--------------------------")

# Declarar a primeira variável:
print("Digite um numero")
num1 = float(input())
# Declarar a segunda variável:
print("Digite outro numero")
num2 = float(input())
# Fazer a soma da primeira variável com a segunda variável
soma  = num1 + num2
# Imprimir na tela
print("{} + {} = {}".format(num1, num2, soma))

print("--------------------------")

div = num1 / num2
print("{}/{} ={}".format)

print("--------------------------")

sub = num1 - num2
print("{} - {} = {}".format(num1, num2, sub))

print("--------------------------")

mult = num1 * num2
print("{} * {} = {}".format(num1, num2, mult))

print("--------------------------")

div = num1 / num2
print("{} / {} = {}".format(num1, num2, div))

print("--------------------------")

div_inteira = num1 // num2
print("{} // {} = {}".format(num1, num2, div_inteira))

print("--------------------------")

mod = num1 % num2
print("{} % {} = {}".format(num1, num2, mod))

exp = num1 ** num2
print("{} ** {} = {}".format(num1, num2, exp))

print("--------------------------")



