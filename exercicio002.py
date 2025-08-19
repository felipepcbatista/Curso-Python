print("==== BEM-VINDO AO BANCO PY ====")

senha_correta = "python123"
tentativas = 3
autenticado = False

# Repete até atingir limite de tentativas (3)
while tentativas > 0:
    senha = input("Digite a senha de acesso: ")

    # Compara senha digitada com senha correta
    if senha == senha_correta:
        print("Acesso concedido.\n")
        autenticado = True # Autentica usuário
        break

    # Executa se senha digitada for diferente da senha correta
    else:
        tentativas -= 1 # Perde uma tentativa
        print("Senha incorreta. Tentativas restantes:", tentativas)

# Executa se o usuário errou nas 3 tentativas
if not autenticado:
    print("Conta bloqueada temporariamente. Tente novamente mais tarde.")

else:
    # Inicialização de variáveis financeiras

    # Saldo
    saldo = 0.0

    # Depósito
    qtd_depositos = 0
    total_depositos = 0.0
    maior_deposito = 0.0

    # Saque
    qtd_saques = 0
    total_saques = 0.0
    maior_saque = 0.0

    # Limites
    limite_por_saque = 500.0
    limite_qtd_saques = 3

    # Loop com Menu
    while True:
        print("\n----MENU DE OPERAÇÕES----")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Saldo")
        print("[4] Relatório do dia")
        print("[5] Sair")

        opcao = int(input("Escolha uma opção: "))

        # DEPÓSITO
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
                          
            if valor > 0:
                saldo += valor
                qtd_depositos += 1
                total_depositos += valor

                # Verifica se o valor depositado é o maior valor até o momento
                if valor > maior_deposito:
                    maior_deposito = valor

                print("Depósito realizado com sucesso!")
            
            # Executa se o valor digitado é inválido para depósito
            else: 
                print("Valor inválido.")
                continue # Volta ao menu
        
        # SAQUE
        elif opcao == 2:

            # Verifica se não atingiu limite de saques
            if qtd_saques < limite_qtd_saques:
                valor = float(input("Digite o valor a ser sacado: "))

                # Verifica se o valor inserido é válido para saque
                if valor > 0 and valor <= saldo and valor <= limite_por_saque:
                    saldo -= valor
                    qtd_saques += 1
                    total_saques += valor

                    #Verifica se o valor sacado é o maior valor até o momento
                    if valor > maior_saque:
                        maior_saque = valor

                    print("Saque realizado com sucesso!")

                # Executa se o valor digitado é inválido para saque
                else:
                    print("Valor inválido.")
                    continue
            
            # Executa se atingiu limite de saques
            else:
                print("Limite diário de saques atingido. Tente novamente outro dia.")
                continue
        
        # SALDO
        elif opcao == 3:
            print(f"Saldo atual: R$ {saldo:.2f}")
            
        # RELATÓRIO
        elif opcao == 4:

            # Depósitos
            print(f"DEPÓSITOS:\nQuantidade total: {qtd_depositos} | Valor total: R$ {total_depositos:.2f} | Maior Valor: R$ {maior_deposito:.2f}\n")

            # Saques
            print(f"SAQUES:\nQuantidade total: {qtd_saques} | Valor total: R$ {total_saques:.2f} | Maior valor: R$ {maior_saque:.2f}\n")

            # Limites
            print(f"LIMITES:\nValor limite por saque: R$ {limite_por_saque:.2f} | Saques restantes: {limite_qtd_saques-qtd_saques}")

            # Saldo
            print(f"SALDO:\nSaldo atual: R$ {saldo:.2f}")

        # ENCERRAR
        elif opcao == 5:
            print("Obrigado, volte sempre!")
            break

        # Opção inválida - Menu
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")
            continue