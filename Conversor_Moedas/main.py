
def converter_Dolar_Euro(valor):
    euro = 6.17
    dolar = 5.71
    dinheiro =  valor * (dolar / (euro))
    print(f"Você converteu ${valor} para €{dinheiro:.2f}!")
    
def converter_Dolar_Real(valor):
    dolar = 1
    real = 5.71
    dinheiro =  valor * (real / dolar)
    print(f"Você converteu ${valor} para R${dinheiro:.2f}!")
    
def converter_Euro_Real(valor):
    euro = 1
    real = 6.17
    dinheiro =  valor * (real / euro)
    print(f"Você converteu €{valor} para R${dinheiro:.2f}!")
    
def converter_Euro_Dolar(valor):
    euro = 6.17
    dolar = 5.71
    dinheiro =  valor * (euro / dolar)
    print(f"Você converteu €{valor} para ${dinheiro:.2f}!")
    
def converter_Real_Dolar(valor):
    real = 5.71
    dolar = 1
    dinheiro =  valor * (dolar / real)
    print(f"Você converteu R${valor} para ${dinheiro:.2f}!")
    
def converter_Real_Euro(valor):
    real = 6.17
    euro = 1
    dinheiro =  valor * (euro / real)
    print(f"Você converteu R${valor} para €{dinheiro:.2f}!")
    
menu = """
    0 - Sair
    1 - Converter Dolar para Euro
    2 - Converter Dolar para Real
    3 - Converter Euro para Real
    4 - Converter Euro para Dolar
    5 - Converter Real para Dolar
    6 - Converter Real para Euro
"""

while True:
    print(menu)

    opcao = input("Escolha uma opção: ").strip()
    
    match opcao:
        case "0":
            print("Saindo...")
            break

        case "1":
            valor = float(input("Digite o valor em Dolar: ").strip())
            converter_Dolar_Euro(valor)
        
        case "2":
            valor = float(input("Digite o valor em Dolar: ").strip())
            converter_Dolar_Real(valor)

        case "3":
            valor = float(input("Digite o valor em Euro: ").strip())
            converter_Euro_Real(valor)

        case "4":
            valor = float(input("Digite o valor em Euro: ").strip())
            converter_Euro_Dolar(valor)

        case "5":
            valor = float(input("Digite o valor em Real: ").strip())
            converter_Real_Dolar(valor)

        case "6":
            valor = float(input("Digite o valor em Real: ").strip())
            converter_Real_Euro(valor)

    