from datetime import datetime

menu1 = """ 

[u] Criar usuario
[c] Abrir conta


=>"""

menu2 = """

[d] Depositar
[s] Sacar
[e] Saldo
[q] Sair


=>"""
cpf = ""
nome = ""
dataNas = ""

listaUser = []
listaConta = []
limite_digitos = 11

opcao1 = input(menu1)
if opcao1 == "u":
    while True:
        nome = input("Informe o seu nome completo: ")

        if nome.isalpha() or all(c.isalpha() or c.isspace() for c in nome):
            print("Nome cadastrado com sucesso!")
            break
        else:
            print("Insira um nome válido!")

    while True:
        cpf = (input("Informe o seu cpf:"))
        if cpf.isdigit() and len(cpf) > limite_digitos or len(cpf) < limite_digitos:
            print("Cpf inválido!")
            exit()
        else:
            print("Cpf cadastrado com sucesso!")
        break

    while True:
        dataNas = input("Informe sua data de nascimento (dd/mm/aaaa): ")

        try:
            if len(dataNas) == 8:  # Verifica se tem 8 dígitos
                dia = int(dataNas[:2])
                mes = int(dataNas[2:4])
                ano = int(dataNas[4:])
                data = datetime(ano, mes, dia)
                print("Data de nascimento cadastrada com sucesso!")
                break
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")

    def addUser(listaUser):
        print(f"Usuário criado com sucesso. Seja bem-vindo {nome.title()}!")
    addUser(listaUser)

while True:
    menu1 = input(menu1)
    if opcao1 == "c":
        CPFconta = input("Insira um CPF cadastrado: ")
        dataConta = input("Insira a data de nascimento: ")
        if CPFconta == cpf and dataConta == dataNas:
            print("CPF válido! ")
            print("Usuário localizado!")
            break
    else:
        print("Usuário não cadastrado ou informações inválidas!")
else:
    print("Operação inválida!")
    exit()




saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
saque_diario  = 3
excedido_saques = 0

while True:
    opcao = input(menu2)
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


