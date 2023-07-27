menu = """

[d] Depositar
[s] Sacar
[e] Saldo
[q] Sair


=>"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
saque_diario  = 3
excedido_saques = 0
while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"
        elif valor < 0:
            print("Operação Inválida.")
        else:
            print("Operação inválida.")


    elif opcao == "s":
        print("Saque")

        saque = float(input("Informe o valor do saque:"))

        if saque > saldo:
            print("Saldo insuficiente")
        elif saque >= 600:
            print("Limite do valor de saque: R$500")
        else:
            numero_saques += 1
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
        print(f"Números de saques diários:{numero_saques}/3")

        if numero_saques > LIMITE_SAQUES:
            while numero_saques >= 3:
                numero_saques -=3
                if numero_saques == 3:
                    print(f"Número de saques diários excedidos:{3}/{LIMITE_SAQUES}")
            break



    elif opcao == "e":
        print(f"Extrato:{saldo}")

    if opcao == "q":
        print("Até mais")
        exit()


