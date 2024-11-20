from dataclasses import replace
import PySimpleGUI as sg
import os
import re

class Conta:
    def __init__(self, id, nome, senha, saldo, extrato):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.saldo = saldo
        self.extrato = extrato

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome
    
    def getSenha(self):
        return self.senha
    
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getExtrato(self):
        return self.extrato
    
    def setExtrato(self, extrato):
        self.extrato = extrato

    def exibirInf(self):
        return f"Id: {self.id}\nNome: {self.nome}\nSenha: {self.senha}\nSaldo: {self.saldo}\nExtrato: {self.extrato}"

def cadastrarConta(contas, id_contador):
    janela_cadastrar = [
        [sg.Text('================ Cadastro ================')],
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')], 
        [sg.Text('', key='mensagem')],
    ]

    window_cadastro = sg.Window('Sistema Bancário', layout=janela_cadastrar)

    while True:
        event, values = window_cadastro.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Cadastrar':
            id = id_contador
            nome = values['usuario'].upper()
            status = True
            
            if nome == "":
                window_cadastro['mensagem'].update('Nome de usuário não pode ser vazio!')
                status = False
            elif nome in [conta.getNome().upper() for conta in contas]:
                window_cadastro['mensagem'].update('Nome de usuário já existe!')
                status = False
            elif nome[0].isdigit():
                window_cadastro['mensagem'].update('Nome de usuário não pode começar com número!')
                status = False
            elif not nome[0].isalpha():
                window_cadastro['mensagem'].update('Nome de usuário deve começar com letra!')
                status = False
            elif re.match(".*[^A-Za-z0-9].*", nome):
                window_cadastro['mensagem'].update('Nome não deve ter caracteres especiais.')
                status = False
            elif len(nome) < 3 or len(nome) > 20:
                window_cadastro['mensagem'].update('Nome de usuário deve ter entre 3 e 20 caracteres!')
                status = False

            novoNome = nome.replace(" ","")
            nome = novoNome

            senha = values['senha']
            if senha == "":
                window_cadastro['mensagem'].update('Senha não pode ser vazia!')
                status = False
            elif len(senha) < 4:
                window_cadastro['mensagem'].update('Senha deve ter pelo menos 4 caracteres!')
                status = False
            
            saldo = 0
            extrato = []

            if status:
                novaConta = Conta(id, nome, senha, saldo, extrato)
                contas.append(novaConta)
                window_cadastro['usuario'].update('')
                window_cadastro['senha'].update('')
                sg.popup("Conta criada com sucesso!")

        elif event == 'Voltar':
            window_cadastro.close()
            telaInicial(contas)
            break


def entrarConta(contas):

    janela_entrar = [
        [sg.Text('================= Entrar =================')],
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Entrar'), sg.Button('Voltar')],
        [sg.Text('', key='mensagem')],
    ]

    window_entrar = sg.Window('Sistema Bancário', layout=janela_entrar)

    while True:
        event, values = window_entrar.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Entrar':
            if contas != []:
                nome = values['usuario'].upper()
                senha = values['senha']
                for conta in contas:
                    if conta.getNome() == nome and conta.getSenha() == senha:
                        window_entrar.close()
                        menuConta(conta, contas)
                        break
                window_entrar['mensagem'].update("Nome ou senha incorretos! Tente novamente.")
            else:
                sg.popup("Nenhuma conta cadastrada!")
                break
        elif event == 'Voltar':
            window_entrar.close()
            telaInicial(contas)
            break


def depositar(contaLogada, contas, saldo, listaExtrato):

    janela_depositar = [
        [sg.Text('================= Depositar =================')],
        [sg.Text(f'Saldo Atual: {saldo:,.2f}', key='saldoAtual')],
        [sg.Text('Valor a ser depositado:')],
        [sg.Input(key='valor')],
        [sg.Button('Depositar'), sg.Button('Voltar')],
        [sg.Text('',key='mensagem')],
    ]

    listaExtrato = contaLogada.getExtrato()

    window_depositar = sg.Window('Sistema Bancário', layout=janela_depositar)

    while True:
        event, values = window_depositar.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Depositar':
            try:
                deposito = float(values['valor'])
                if deposito > 0:
                    saldo += deposito
                    contaLogada.setSaldo(saldo)
                    window_depositar['saldoAtual'].update(f"Saldo Atual: {saldo:,.2f}")
                    extrato = "Depóstido de " + (f"R${deposito:,.2f}")
                    listaExtrato.append(extrato)
                    contaLogada.setExtrato(listaExtrato)
                    sg.popup("Depósito realizado com sucesso!")
                else:
                    window_depositar['mensagem'].update("Valor inválido! Tente novamente.")
            except ValueError:
                window_depositar['mensagem'].update("Valor inválido! Digite apenas números.")

            window_depositar['valor'].update('')

        elif event == 'Voltar':
            window_depositar.close()
            menuConta(contaLogada, contas)
            break

def sacar(contaLogada, contas, saldo, listaExtrato):

    janela_sacar = [
        [sg.Text('================= Sacar =================')],
        [sg.Text(f'Saldo Atual: {saldo:,.2f}', key='saldoAtual')],
        [sg.Text('Valor a ser sacado:')],
        [sg.Input(key='valor')],
        [sg.Button('Sacar'), sg.Button('Voltar')],
        [sg.Text('',key='mensagem')],
    ]

    window_sacar = sg.Window('Sistema Bancário', layout=janela_sacar)
    LIMITE_SAQUE = 500
    listaExtrato = contaLogada.getExtrato()

    while True:
        event, values = window_sacar.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Sacar':
            try:
                if saldo > 0:
                    saque = float(values['valor'])
                    if saque > LIMITE_SAQUE:
                        window_sacar['mensagem'].update("Valor de saque excede o limite de R$500,00. Saque não realizado!")
                    elif saque > saldo or saque <= 0:
                        window_sacar['mensagem'].update("Valor Inválido. Saque não realizado!")
                    else:
                        saldo -= saque
                        contaLogada.setSaldo(saldo)
                        window_sacar['saldoAtual'].update(f"Saldo Atual: {saldo:,.2f}")
                        extrato = "Saque de " + (f"R${saque:,.2f}")
                        listaExtrato.append(extrato)
                        contaLogada.setExtrato(listaExtrato)    
                        window_sacar['mensagem'].update('')
                        sg.popup(f"\nSaque realizado com sucesso!")
                else:
                    sg.popup("Saldo insuficiente. Por favor, tente novamente.")

            except ValueError:
                window_sacar['mensagem'].update("Valor inválido! Digite apenas números.")

            window_sacar['valor'].update('')

        elif event == 'Voltar':
            window_sacar.close()
            menuConta(contaLogada, contas)
            break

def transferir(contaLogada, contas, saldo, listaExtrato):

    janela_transferir = [
        [sg.Text('================= Transferir =================')],
        [sg.Text(f'Saldo Atual: {saldo:,.2f}', key='saldoAtual')],
        [sg.Text('Id destino:')],
        [sg.Input(key='id_destino')],
        [sg.Text('Valor a ser transferido:')],
        [sg.Input(key='valor')],
        [sg.Button('Enviar'), sg.Button('Voltar')],
        [sg.Text('',key='mensagem')],
    ]

    window_transferir = sg.Window('Sistema Bancário', layout=janela_transferir)

    while True:
        event, values = window_transferir.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Enviar':
            if saldo > 0:
                try:
                    status = False
                    propriaConta = False
                    contaNaoEncontrada = True
                    id_destino = int(values['id_destino'])
                    for conta in contas:
                        if id_destino == conta.getId():
                            contaNaoEncontrada = False
                            if contaLogada.getId() == id_destino:
                                propriaConta = True
                            else:
                                status = True
                                valor = float(values['valor'])
                                saldoConta = conta.getSaldo()
                                extratoConta = conta.getExtrato()
                                if valor > 0:
                                    novoValor = saldoConta + valor
                                    conta.setSaldo(novoValor)
                                    extratoConta.append(f"Recebeu R${valor:,.2f} de {contaLogada.getNome()}")
                                    conta.setExtrato(extratoConta)

                                    saldo -= valor
                                    contaLogada.setSaldo(saldo)
                                    window_transferir['saldoAtual'].update(f'Saldo Atual: {saldo:,.2f}')
                                    extrato = f"Enviou R${valor:,.2f} para {conta.getNome()}"
                                    listaExtrato.append(extrato)
                                    contaLogada.setExtrato(listaExtrato)

                                else:
                                    window_transferir['mensagem'].update("Valor Inválido! Tente novamente.")
                                    break

                            if status:
                                window_transferir['mensagem'].update('')
                                sg.popup("Transferência concluída com sucesso!")
                            elif propriaConta:
                                window_transferir['mensagem'].update("Você não pode transferir para si mesmo!")
                    if contaNaoEncontrada:
                        window_transferir['mensagem'].update("Conta não encontrada! Tente novamente.")
                except ValueError:
                    window_transferir['mensagem'].update("Valor Inválido! Tente novamente.")
            
            else:
                window_transferir['mensagem'].update("Saldo insuficiente. Por favor, tente novamente.")

            window_transferir['id_destino'].update('')
            window_transferir['valor'].update('')

        elif event == 'Voltar':
            window_transferir.close()
            menuConta(contaLogada, contas)
            break
                
def verExtrato(contaLogada, contas, listaExtrato):

    janela_verExtrato = [
        [sg.Text('=============== Extrato ===============')],
        [sg.Listbox(values=[], size=(40, 10), key='lista_extrato')],
        [sg.Button('Atualizar'), sg.Button('Voltar')],
    ]

    window_verExtrato = sg.Window('Extrato', janela_verExtrato)

    while True:
        event, values = window_verExtrato.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Atualizar':
            if listaExtrato == []:
                window_verExtrato['lista_extrato'].update(['Não há extrato disponível.'])
            else:
                window_verExtrato['lista_extrato'].update(listaExtrato)
        elif event == 'Voltar':
            window_verExtrato.close()
            menuConta(contaLogada, contas)
            break


    else:
        for i in range(len(extrato)):
            print(extrato[i])



def verContas(contas):
    janela_verContas = [
        [sg.Text('=================== CONTAS ===================')],
        [sg.Listbox(values=[], size=(50, 10), key='lista_contas')],
        [sg.Button('Atualizar'), sg.Button('Voltar')],
    ]

    window_verContas = sg.Window('Sistema Bancário', layout=janela_verContas)

    while True:
        event, values = window_verContas.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Atualizar':
            if contas != []:
                lista = []
                for conta in contas:
                    dados_conta = (
                        f"Id: {conta.getId()} | "
                        f"Nome: {conta.getNome()} | "
                        f"Senha: {conta.getSenha()} | "
                        f"Saldo: {conta.getSaldo()} | "
                        f"Extrato: {'Não há extrato disponível.' if conta.getExtrato() == [] else 'Extrato disponível.'}"
                    )
                    lista.append(dados_conta)

                window_verContas['lista_contas'].update(lista)
            else:
                sg.popup("Nenhuma conta registrada!")
        elif event == 'Voltar':
            window_verContas.close()
            telaInicial(contas)
            break


def menuConta(contaLogada, contas):
    nome = contaLogada.getNome()
    saldo = contaLogada.getSaldo()
    extrato = contaLogada.getExtrato()

    janela_menu = [
        [sg.Text(f'========== Conta Logada: {nome} ==========')],
        [sg.Text(f'Bem-vindo, {nome}!')],
        [sg.Text(f'Saldo: R$ {saldo:,.2f}')],
        [sg.Button('Depositar')],
        [sg.Button('Sacar')],
        [sg.Button('Transferir')],
        [sg.Button('Extrato')],
        [sg.Button('Voltar')],
    ]

    window_menu = sg.Window('Menu Conta', layout=janela_menu)

    while True:
        event, values = window_menu.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Depositar':
            window_menu.close()
            depositar(contaLogada, contas, saldo, extrato)
            break
        elif event == 'Sacar':
            window_menu.close()
            sacar(contaLogada, contas, saldo, extrato)
            break
        elif event == 'Transferir':
            window_menu.close()
            transferir(contaLogada, contas, saldo, extrato)
            break
        elif event == 'Extrato':
            window_menu.close()
            verExtrato(contaLogada, contas, extrato)
        elif event == 'Voltar':
            window_menu.close()
            entrarConta(contas)
            break


def telaInicial(contas):
    id_contador = len(contas)
    tela_inicial = [
        [sg.Text('Seja Bem Vindo ao Sistema Bancário!')],
        [sg.Button('Cadastrar')],
        [sg.Button('Entrar')],
        [sg.Button('Ver Contas')],
    ]

    window = sg.Window('Sistema Bancário', layout=tela_inicial)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Cadastrar':
            window.close()
            cadastrarConta(contas, id_contador)
        elif event == 'Entrar':
            window.close()
            entrarConta(contas)
        elif event == 'Ver Contas':
            window.close()
            verContas(contas)

contas = []
conta1 = Conta(0,"DIGO", "1234", 100, [])
conta2 = Conta(1,"JOHN", "1234", 0, [])
contas.append(conta1)
contas.append(conta2)

telaInicial(contas)