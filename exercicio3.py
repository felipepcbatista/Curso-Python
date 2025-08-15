from random import shuffle

lista = []
for i in range(4):
    nome = input(f"Aluno {i+1}: ")
    lista.append(nome)

shuffle(lista)

print("A ordem de apresentação será:")
for aluno in lista:
    print(aluno)
