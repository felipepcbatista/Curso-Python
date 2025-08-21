senha_correta = "python123"
tentativas = 0
while tentativas < 3:
    senha = str(input("Digite a senha de acesso: "))
    tentativas += 1
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        if tentativas == 3:
            print("Conta bloqueada.")
        else:
            print(f"Senha incorreta. Você tem mais {3 - tentativas} tentativa(s).")