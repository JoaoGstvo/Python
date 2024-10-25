
import pyautogui
import time

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1.5)


# Passo 2: Fazer login
pyautogui.press("tab")

pyautogui.write("joaojogos2609@gmail.com")  
pyautogui.press("tab")

pyautogui.write("suasenha")
pyautogui.press("tab")

pyautogui.press("enter")
time.sleep(4)

# Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("Aula1\produtos.csv")

# print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:

    pyautogui.click(x=492, y=275)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter") 

    pyautogui.scroll(5000)
