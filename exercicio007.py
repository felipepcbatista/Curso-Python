# Importa shuffle da biblioteca random para embaralhar a ordem
from random import shuffle

# Declara lista
pessoas = []

# Inicializa lista
for i in range (5):
    nome = str(input(f"Digite o nome da {i+1}ª pessoa: "))
    pessoas.append(nome)

# Embaralha lista
shuffle(pessoas)
print(pessoas)

# Converte em tuple
pessoas_tuple = tuple(pessoas)
print(pessoas_tuple)