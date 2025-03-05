nome = input('Digite seu nome: ')

saldo = 0.0
limite_qtd_saque = 3
LIMITE_SAQUE = 500.00
extrato = []

print(f"Olá, {nome}! Vamos dar início ao seu atendimento.")

while True:
    try:
        atendimento = int(input(f"\nSeu Saldo Atual é de R$ {saldo:.2f}\n"
                                "Qual opção você gostaria de utilizar?\n"
                                "1 - DEPÓSITO\n2 - SAQUE\n3 - EXTRATO\n4 - SAIR\nEscolha: "))

        match atendimento:

            case 1:
                print("Opção DEPÓSITO selecionada")
                deposito = float(input("Quanto você gostaria de depositar? R$ "))

                if deposito <= 0:
                    print("Valor inválido! O depósito deve ser maior que zero.")
                else:
                    saldo += deposito
                    extrato.append(f"Depósito: +R$ {deposito:.2f}")
                    print(f"Operação realizada com sucesso!\nSeu Saldo atual é de R$ {saldo:.2f}")

            case 2:
                if limite_qtd_saque == 0:
                    print("Você atingiu o limite diário de saques!")
                    continue  # Volta para o menu

                print("Opção SAQUE selecionada")
                saque = float(input(f"Quanto você gostaria de sacar? (Limite por saque: R$ {LIMITE_SAQUE:.2f}) R$ "))

                if saque > LIMITE_SAQUE:
                    print(f"Valor maior do que o permitido (Máximo R$ {LIMITE_SAQUE:.2f})")

                elif saque > saldo:
                    print("Saldo insuficiente!")

                elif saque <= 0:
                    print("Valor inválido! O saque deve ser maior que zero.")

                else:
                    saldo -= saque
                    limite_qtd_saque -= 1
                    extrato.append(f"Saque: -R$ {saque:.2f}")
                    print(f"Operação realizada com sucesso!\nSeu Saldo atual é de R$ {saldo:.2f}")

            case 3:
                print("\n========== EXTRATO ==========")
                if not extrato:
                    print("Nenhuma movimentação realizada.")
                else:
                    for operacao in extrato:
                        print(operacao)
                print(f"Saldo atual: R$ {saldo:.2f}")
                print("==============================")

            case 4:
                print("Você escolheu a opção SAIR\nFoi um prazer lhe atender!")
                break

            case _:
                print("Opção inválida, tente novamente.")

    except ValueError:
        print("Por favor, digite um número válido.")
