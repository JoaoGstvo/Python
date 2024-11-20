import os

def depositar(saldo):
    deposito = float(input("Informe o valor a ser depositado: "))
    extrato = ""
    if deposito >= 1:
        saldo += deposito
        extrato = f"Depósito de R${deposito:.2f}"
        print(f"Depósito realizado com sucesso! Saldo atual: {saldo}")
    else:
        print("Valor inválido. Por favor, insira um valor maior que 1.")

    return saldo, extrato


def sacar(saldo):
    LIMITE_VALOR = 500
    extrato = ""
    saque = float(input("Informe o valor a ser sacado: "))

    if saque >= float(1) and saque <= LIMITE_VALOR and saque <= saldo:
        saldo -= saque
        extrato = f"Saque de R${saque:.2f}"
        print(f"Saque realizado com sucesso! Seu saldo atual é de: {saldo}")
    else:
        print("Saque não autorizado. Por favor, verifique o valor ou se seu limite diário já foi alcançado!")

    return saldo, extrato


def ver_extrato(extrato):
    print("⊰᯽⊱┈──╌♤ EXTRATO ♤╌──┈⊰᯽⊱")
    if not extrato:
        print("Nenhum movimento realizado.")
    else:
        for i in range(len(extrato)):
            print(extrato[i])

    return extrato


def criar_conta(identificador_conta):
    conta = {
        "id": identificador_conta,
        "nome": input("Digite seu nome: "),
        "senha": input("Crie sua senha (Apenas letras): "),
        "saldo": 0,
        "extrato": []
    }
    return conta


saldo = 0
extrato = []
contas = {}
LIMITE_DIARIO = 3
i = 0
SENHA_ADM = "ADM"

identificador_conta = 0

while True:
    
    menu = f"""
        ⊰᯽⊱┈──╌♤ MENU ♤╌──┈⊰᯽⊱
        Saldo: R${saldo:.2f}
        [c]Criar Conta
        [d]Depositar
        [s]Sacar
        [e]Extrato
        [q]Sair
        [A]ADM
        => """
    print(menu)
        
    opcao = input("Opção: ")

    match opcao:

        case "c":
            os.system('cls')
            identificador_conta += 1
            nova_conta = criar_conta(identificador_conta)
            contas[identificador_conta] = nova_conta
            print(f"Conta criada com sucesso! ID da conta: {identificador_conta}")

        case "d":
            os.system('cls')
            saldo, extrato_atual = depositar(saldo)
            extrato.append(extrato_atual)

        case "s":    
            os.system('cls')
            if i == LIMITE_DIARIO:  
                print("Limite diário de saques alcançado!")
            else:
                i +=  1
                saldo, extrato_atual = sacar(saldo)
                extrato.append(extrato_atual)

        case "e":
            os.system('cls')
            ver_extrato(extrato)

        case "A":
            os.system('cls')
            senha = input("Digite a senha: ")

            if senha == SENHA_ADM:
                os.system('cls')
                menu_adm = f"""
        ⊰᯽⊱┈──╌♤ MENU ADM ♤╌──┈⊰᯽⊱

        [c]Visualizar Contas
        [r]Remover Conta
        => """
                print(menu_adm)
                opcao_adm = input("Opção: ")

                match opcao_adm:
                    case "c":
                        os.system('cls')
                        if contas:
                            for id_conta, conta in contas.items():
                                print(f"ID: {id_conta}, Nome: {conta['nome']}, Saldo: R${conta['saldo']:.2f}")
                        else:
                            print("Nenhuma conta cadastrada.")

                    case "r":
                        os.system('cls')
                        id_remover = int(input("Informe o ID da conta a ser removida: "))
                        if id_remover in contas:
                            del contas[id_remover]
                            print(f"Conta ID {id_remover} removida com sucesso!")
                        else:
                            print("Conta não encontrada!")

        case "q":
            os.system('cls')
            print("Saindo...")
            break

        case _:
            os.system('cls') 
            print("Opção inválida! Tente novamente.")
