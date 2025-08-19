# Importa string para uso de punctuation
import string

frase = str(input("Digite uma frase: "))

# Remove pontuações da frase com translate e maketrans
tabela = frase.maketrans('', '', string.punctuation) # Cria tabela de regras
sem_pontuacao = frase.translate(tabela) # Aplica tabela

# Divide a frase a cada espaço
palavras = sem_pontuacao.split(' ')

# Conta a frequência de letra 'a' na frase
frequencia_a = sem_pontuacao.count('a')

# Altera o case dos caracteres
minusculas = frase.lower()
maiusculas = frase.upper()
capitalizada = frase.title()

# Imprime alterações
print(f"Palavras existentes na frase: {palavras}\nFrase em UpperCase: {maiusculas}\nFrase em LowerCase {minusculas}\nFrase em Capitalize: {capitalizada}\nFrequência de letra \'a\': {frequencia_a}")