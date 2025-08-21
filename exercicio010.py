senha_correta = "python123"
tentativas = 3
autenticado = False

while tentativas > 0:
    senha = (input("Digite a senha de acesso: "))
    if senha == senha_correta:
        print("Seja bem-vindo!")
        autenticado = True
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você tem mais {tentativas} tentativas.")

if not autenticado:
    print("Conta bloqueada temporariamente. Tente novamente mais tarde.")

else: 
    # Depósitos
    depositos = []
    qtd_depositos = 0

    # Saques
    saques = []
    qtd_saques = 0

    # Limites
    limite_saque_dia = 3
    limite_maximo_saque = 500

    # Saldo
    saldo = 0.0

    while True:
        print("\n==== MENU DE OPÇÕES ====")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Saldo")
        print("[4] Relatório do dia")
        print("[0] Sair")

        operacao = (input("Escolha uma opção: "))

        match operacao:
            case '1':
                valor = float(input("Digite o valor a ser depositado: "))
                if valor <= 0:
                    print("Valor inválido.")
                    continue
                qtd_depositos += 1
                saldo += valor
                depositos.append(valor)
            case '2':
                if qtd_saques >= limite_saque_dia:
                    print("Limite de saques diário atingido. Tente novamente mais tarde.")
                    continue
                else:
                    valor = float(input("Digite o valor a ser sacado: "))
                    if valor <= 0 or valor > saldo or valor > limite_maximo_saque:
                        print("Valor inválido.")
                        continue
                    qtd_saques += 1
                    saldo -= valor
                    saques.append(valor)                               
            case '3':
                print(f"Saldo: R$ {saldo:.2f}")
            case '4':
                maior_deposito = max(depositos)
                maior_saque = max(saques)
                print(f"----DEPÓSITOS----\nHistórico: {[f'R$ {valor:.2f}' for valor in depositos]}\nQuantidade total: {qtd_depositos}\n Maior valor: R$ {maior_deposito:.2f}\n----SAQUES----\nHistórico: {[f'R$ {valor:.2f}' for valor in saques]}\nQuantidade total: {qtd_saques}\nMaior valor: R$ {maior_saque:.2f}\n----LIMITES----\nSaques restantes de hoje: {limite_saque_dia-qtd_saques}\n----SALDO----\nSaldo atual: R$ {saldo:.2f}")
            case '0':
                print("Encerrando...")
                break
            case _:
                print("Opção inválida.")
            
