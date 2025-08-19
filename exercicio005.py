# Recebe entrada para cor
cor = str(input("Cor do semáforo (Verde, Amarelo ou Vermelho): "))

# Padroniza entrada
cor = cor.strip().lower()

# Match-case para verificar valor de entrada
match cor:
    case "verde":
        print("Pode passar!")
    case "amarelo":
        print("Atenção!")
    case "vermelho":
        print("Pare!")
    case _:
        print("Cor inválida.")