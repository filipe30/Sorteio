import random
pri=str(input("Digite um nome"))
seg=str(input("Digite um nome"))
ter=str(input ("Digite um nome"))
qua=str(input('Digite um nome'))
lista=[pri ,seg, ter, qua]
esc=random.choice(lista)
print(f'O escolido foi{esc}')