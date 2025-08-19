from random import shuffle

pessoas = []
for i in range (5):
    nome = str(input(f"Digite o nome da {i+1}ª pessoa: "))
    pessoas.append(nome)

shuffle(pessoas)
print(pessoas)

pessoas_tuple = tuple(pessoas)
print(pessoas_tuple)