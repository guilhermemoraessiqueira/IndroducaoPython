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

