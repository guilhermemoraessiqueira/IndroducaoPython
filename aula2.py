# Colocar 7 == 7, verificar a resposta na execussão do programa;
print(7 == 7)
# Colocar 7 == 5, verificar a resposta na execussão do programa;
print(7 == 5)

print("----------------------")

# Colocar 7 < 7, verificar a resposta na execussão do programa;
print(7 < 7)
# Colocar 7 < 10, verificar a resposta na execussão do programa;
print(7 < 10)
# Colocar 7 > 7, verificar a resposta na execussão do programa;
print(7 > 7)
# Colocar 7 > 5, verificar a resposta na execussão do programa;
print(7 > 5)

print("----------------------")

# Colocar 7 <= 7, verificar a resposta na execussão do programa;
print(7 <= 7)
# Colocar 7 <= 10, verificar a resposta na execussão do programa;
print(7 <= 10)
# Colocar 7 >= 7, verificar a resposta na execussão do programa;
print(7 >= 7)
# Colocar 7 >= 5, verificar a resposta na execussão do programa;
print(7 >= 7)

print("----------------------")

# Colocar 7 != 7, verificar a resposta na execussão do programa;
print(7 != 7)
# Colocar 7 != 5, verificar a resposta na execussão do programa;
print(7 != 7)

print("----------------------")

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False and False,"|")
print("|",True,"\t|",False,"|",True and False,"|")
print("|",False,"|",True,"\t|",False and True,"|")
print("|",True,"\t|",True,"\t|",True and True,"\t|")

print("----------------------")


# EXEMPLO: Verificar se uma idade é maior do que a 17 E menor do que 71.

idade = int(input("Idade: "))
print(idade > 17 and idade < 71)

print("----------------------")

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False or False,"|")
print("|",True,"\t|",False,"|",True or False," |")
print("|",False,"|",True,"\t|",False or True," |")
print("|",True,"\t|",True,"\t|",True or True," |")

print("----------------------")

# EXEMPLO: Verificar se uma idade é menor do que a 18 OU maior do que 70.

idade = int(input("Idade: "))
print(idade < 18 or idade > 70)

print("----------------------")

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False ^ False,"|")
print("|",True,"\t|",False,"|",True ^ False,"\t|")
print("|",False,"|",True,"\t|",False ^ True,"\t|")
print("|",True,"\t|",True,"\t|",True ^ True,"|")


print("----------------------")

# Reprodução de porcos
# Coloque 0 para leitão e 1 para leitoa em uma lista
leitao = 0
porquinha = 1
print("{} com {} é {}".format(leitao, leitao, leitao^leitao))
print("{} com {} é {}".format(porquinha, leitao, porquinha^leitao))
print("{} com {} é {}".format(leitao, porquinha, leitao^porquinha))
print("{} com {} é {}".format(porquinha, porquinha, porquinha^porquinha))

print("----------------------")

print("|   A\t| Não A |")
print("|",False,"|",not False,"\t|")
print("|",True,"\t|",not True,"|")

print("----------------------")

n = 3
if n == 2:
    print("{} igual a 2".format(n))


print("----------------------")

n = 3
if n == 2:
    print("{} igual a 2".format(n))
else:
    print("{} diferente a 2".format(n))

print("----------------------")

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
     
print("----------------------")

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

print("----------------------")

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

print("----------------------")

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

print("----------------------")



print("----------------------")