print("VELOCIDADE EM MPS")
mps = float(input())
kmh = mps * 3.6
print("VELOCIDADE EM KMH", kmh)

print()
print("==================")
print()

import math

print("DIGITE O RAIO DA CIRCUFERENCIA")
raio = float(input())
comprimento = 2 * math.pi * raio
print("O comprimento da circunferência é:", comprimento)

print()
print("==================")
print()

print("DIGITE UM NÚMERO")
entrada = float(input())
antecessor = entrada -1
sucessor = entrada +1
print('''O sucessor é: {}
"O antecessor é: {}'''.format(sucessor,antecessor))

print()
print("==================")
print()

import datetime

print("DIGITE O ANO EM QUE VOCÊ NASCEU")
anoNasc = int(input())
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNasc
print("Sua idade é:", idade, "anos")

