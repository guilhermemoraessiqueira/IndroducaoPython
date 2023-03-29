# Colocar 7 == 7, verificar a resposta na execussão do programa;
print(7 == 7)
# Colocar 7 == 5, verificar a resposta na execussão do programa;
print(7 == 5)

"""####2. Operadores menor que (<) e maior que (>)
"""

# Colocar 7 < 7, verificar a resposta na execussão do programa;
print(7 < 7)
# Colocar 7 < 10, verificar a resposta na execussão do programa;
print(7 < 10)
# Colocar 7 > 7, verificar a resposta na execussão do programa;
print(7 > 7)
# Colocar 7 > 5, verificar a resposta na execussão do programa;
print(7 > 5)

"""####3. Operadores menor ou igual que (<) e maior ou igual que (>)"""

# Colocar 7 <= 7, verificar a resposta na execussão do programa;
print(7 <= 7)
# Colocar 7 <= 10, verificar a resposta na execussão do programa;
print(7 <= 10)
# Colocar 7 >= 7, verificar a resposta na execussão do programa;
print(7 >= 7)
# Colocar 7 >= 5, verificar a resposta na execussão do programa;
print(7 >= 7)

"""####4. Operador de diferente (!=)"""

# Colocar 7 != 7, verificar a resposta na execussão do programa;
print(7 != 7)
# Colocar 7 != 5, verificar a resposta na execussão do programa;
print(7 != 7)

"""##2 - Tabelas Verdade
São tabelas que mostram algumas situações de entrada e suas saídas
####1. Tabela do E (AND)
O operador **AND** deve ser usado quando temos 2 ou mais condições que devem ser verdadeiras para o programa executar a ação desejada
"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False and False,"|")
print("|",True,"\t|",False,"|",True and False,"|")
print("|",False,"|",True,"\t|",False and True,"|")
print("|",True,"\t|",True,"\t|",True and True,"\t|")

# EXEMPLO: Verificar se uma idade é maior do que a 17 E menor do que 71.

idade = int(input("Idade: "))
print(idade > 17 and idade < 71)

"""####2. Tabela do OU (OR)
O operador **OR** deve ser usado quando, pelo menos, 1 das condições for verdadeira para realizar uma ação desejada
"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False or False,"|")
print("|",True,"\t|",False,"|",True or False," |")
print("|",False,"|",True,"\t|",False or True," |")
print("|",True,"\t|",True,"\t|",True or True," |")

# EXEMPLO: Verificar se uma idade é menor do que a 18 OU maior do que 70.

idade = int(input("Idade: "))
print(idade < 18 or idade > 70)

"""####3. Tabela do XOR (^)"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False ^ False,"|")
print("|",True,"\t|",False,"|",True ^ False,"\t|")
print("|",False,"|",True,"\t|",False ^ True,"\t|")
print("|",True,"\t|",True,"\t|",True ^ True,"|")

# Reprodução de porcos
# Coloque 0 para leitão e 1 para leitoa em uma lista
leitao = 0
porquinha = 1
print("{} com {} é {}".format(leitao, leitao, leitao^leitao))
print("{} com {} é {}".format(porquinha, leitao, porquinha^leitao))
print("{} com {} é {}".format(leitao, porquinha, leitao^porquinha))
print("{} com {} é {}".format(porquinha, porquinha, porquinha^porquinha))

"""####4. Tabela de Negação (not)"""

print("|   A\t| Não A |")
print("|",False,"|",not False,"\t|")
print("|",True,"\t|",not True,"|")

"""##3 - Condicionais
#### Condição SE (IF)
Usamos este tipo de condicional quando necessitamos que o programa teste algumas condições. Caso a condição seja verdadeira, o programa executará uma ação destinada àquela condição.
```
if condição 1:
    bloco de códigos do if
```
Faz-se necessário que o código tenha esta estrutura, senão o Python apresentará erro de identação.
"""

n = 3
if n == 2:
    print("{} igual a 2".format(n))

"""#### Condição SENÃO (ELSE)
Para usar o else, temos que ter usado o if antes.
```
if condição 1:
    bloco de códigos do if
    
else:
    bloco de código do else.
    Aqui finaliza a condicional
```
"""

n = 3
if n == 2:
    print("{} igual a 2".format(n))
else:
    print("{} diferente a 2".format(n))

"""#### Condição SENÃO SE (ELIF)
O elif deve ser utilizado quando temos mais do que uma condição.
```
if condição 1:
    bloco de códigos do if
elif condição 2:
    bloco de código do elif
    
else:
    bloco de código do else.
    Aqui finaliza a condicional
```
"""



"""##4 - Exercícios
###1 - Qual o maior.
*Escreva um programa que recebe 2 valores e devolve o maior entre eles.*
"""

# Declaração da variável 1
num_1 = int(input("1º número: "))
# Declaração da variável 2
num_2 = int(input("2º número: "))
# Imprimir na tela mensagem: "O X é maior do que o Y"
if num_1 > num_2:
    print("{} é maior do que {}".format(num_1, num_2))
elif num_2 > num_1:
    print("{} é maior do que {}".format(num_2, num_1))
else:
    print("São iguais")

"""### 2 - Calculadora de preço da laranja.
*Cada laranja custa R\$ 0,3. Mas quando compradas acima de uma dúzia, seu valor cai para R\$ 0,25 cada*
"""

# Declarar a entrada da quantidade de laranjas a ser comprada
laranjas = int(input("Quantas laranjas deseja comprar?\n "))
# Declaração de if
if laranjas < 12:
    valor = laranjas * 0.3
# Declaração else
else:
    valor = laranjas * 0.25
# Imprimir na tela a mensagem: "x laranjas por Y reais totaliza: R$ Z"
print("Você deve pagar R$ {:.2f}".format(valor))

"""###3 - Caluladora de Peso Ideal 
Fazer uma calculadora em que o usuário digita Altura em metros e Peso em quilos e se é do sexo biológico Masculino ou Feminino. O programa devolve ao usuário a informação qual seu peso ideal e quando precisa emagrecer para chegar lá. 
Ao final, o programa deve trazer uma frase motivadora para aqueles que estão acima do peso, frase parabenizando os que estão no peso ideal e uma outra frase de alerta aos que estão abaixo do peso.
***Fórmulas***
        >Masculino: (72.7 * Altura) - 50
        >Feminino: (62.1 * Altura) - 44.7
"""

# Declarar a entrada da Altura
altura = float(input("Altura: "))
# Declarar a entrada do Peso
peso = float(input("Pesoa atual:"))
# Declarar a entrada do Sexo Biológico
sexo = input("M - Masculino ou F - Feminino: ").casefold()
# Declaração de if para calcular peso ideal
if sexo == 'm':
    peso_ideal = (72.7 * altura) - 50
# Declaração de elif para calcular peso ideal
elif sexo == 'f':
    peso_ideal = (62.1 - altura) -44.7
# Declaração else
else:
    print("Digite M para masculino ou F para feminino.")
# Calcular diferença entre peso ideal e peso atual
diferenca = peso - peso_ideal
# Declaração de if para acima do peso - A devolutiva para o usuário vem dentro do if
if diferenca > 0:
    print("Você está acima do peso, mas não desanime. você consegue")
# Declaração de elif para abaixo do peso - A devolutiva para o usuário vem dentro do elif
elif diferenca < 0:
    print("Você está abaixo do peso, faça seus exames periodicamente.")
# Declaração de else - A devolutiva para o usuário vem dentro do else
else:
    print("Muito bem, você está no peso ideal")

"""###4 - É triangulo ou Não é triângulo?
Para determinar se 3 segmentos de reta formam um triângulo, podemos fazer a verificação se a soma dos dois menores segmentos é maior do que o segmento maior.
---
    Segmentos: 2, 3 e 4
    Soma dos dois menores: 2 + 3 = 5
    Verificação: 5 > 4
    Conclusão:Estes segmentos formam um triângulo
---
"""

soma = 0
maior = 0
# Declaração do primeiro segmento
seg_a = float(input("Primeira medida: "))
# Declaração do segundo segmento
seg_b = float(input("Segunda medida: "))
# Declaração do terceiro segmento
seg_c = float(input("Terceira medida: "))
# Neste if, usar AND para avaliar se o 1º segmento é o maior
if seg_a > seg_b and seg_a > seg_c:
    maior = seg_a
    soma = seg_b + seg_c
# Neste elif, usar AND para avaliar se o 2º segmento é o maior
if seg_b > seg_a and seg_b > seg_c:
    maior = seg_b
    soma = seg_a + seg_c
# Neste elif, usar AND para avaliar se o 3º segmento é o maior
if seg_c > seg_a and seg_c > seg_b:
    maior = seg_c
    soma = seg_b + seg_a
# Else para possíveis erros de digitação
else:
    print("Você precisa digitar corretamente")
# Verificação se é triângulo e informar ao usuário.
if soma > maior:
    print("Forma triângulo")
else:
    print("Não forma triângulo")