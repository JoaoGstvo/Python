import os

os.chdir(r"C:\Users\other\OneDrive\Documentos\PYTHONPROJECTS\Tarefas")

lista = [{'Nome': 'nawjnd', 'Descrição': 'dwadaw', 'Concluída': False}, {'Nome': 'dawdwada', 'Descrição': 'dawdawdwa', 'Concluída': False}, {'Nome': 'dadwad', 'Descrição': '1dawdwad', 'Concluída': False}, {'Nome': 'nawjnd', 'Descrição': 'dwadaw', 'Concluída': False}, {'Nome': 'dawdwada', 'Descrição': 'dawdawdwa', 'Concluída': False}, {'Nome': 'dadwad', 'Descrição': '1dawdwad', 'Concluída': False}, {'Nome': 'nawjnd', 'Descrição': 'dwadaw', 'Concluída': False}, {'Nome': 'dawdwada', 'Descrição': 'dawdawdwa', 'Concluída': False}, {'Nome': 'dadwad', 'Descrição': '1dawdwad', 'Concluída': False}]

status = False

menu = """
    ============== MENU ================
    [0]Sair 
    [1]Incluir Tarefa
    [2]Marcar Feito
    [3]Mostrar Tarefas
    [4]Apagar Tarefas
    [5]Salvar
    ====================================
"""

while True:


    print(menu)

    opcao = int(input("O que você deseja fazer: "))

    match opcao:
        case 0:
            break

        case 1:

            tarefa = {
                "Nome": input("Digite o nome da tarefa: "),
                "Descrição": input("Digite a descrição da tarefa: "),
                "Concluída": False
            }
            lista.append(tarefa)

            print("Tarefa adicionada com sucesso!")

        case 2:  

            numero_tarefa = 0

            with open("tarefas.txt", "r") as arq:

                for linha in arq:
                    print(f'({numero_tarefa}) {linha}')
                    numero_tarefa += 1

                feita = int(input("Qual tarefa você deseja finalizar: "))

                for i in range(0, len(lista)):
                    if i == feita:
                        print(f"Tarefa {i} marcada como concluída!")
                        lista[i]["Concluída"] = True

        case 3:

            numero_tarefa = 0

            with open("tarefas.txt", "r") as arq:

                for linha in arq:
                    print(f'({numero_tarefa}) {linha}')
                    numero_tarefa += 1
                

        case 4:
            with open("tarefas.txt", "r", encoding="latin-1") as arq:
                conteudo = arq.readlines()
                for i in range(len(conteudo)):
                    print(f"{i} - {conteudo[i]}")
                    
                apagar = int(input("Insira o número da tarefa que deseja excluir: "))

                for i in range(len(conteudo)):
                    if i == apagar:
                        lista.pop(apagar)
                        status = True
                        break

            if status:
                print("Removido com sucesso!")
            else:
                print("Não encontrado")


        case 5:

            with open("tarefas.txt", "w") as arq:

                for i in range(0, len(lista)):
                    arq.write(f"Tarefa: {lista[i]}\n")
                

