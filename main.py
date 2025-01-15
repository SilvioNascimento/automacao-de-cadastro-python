import pandas as pd
import pyautogui
from time import sleep

# Importar a base de produtos
produtos = pd.read_csv("./database/produtos.csv")

# definir o tempo de espera entre os comandos do PyAutoGUI
pyautogui.PAUSE = 1

# abrir sistema no chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=918, y=352)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar carregar
sleep(5)

# fazer login
pyautogui.click(x=432, y=412)
pyautogui.write("silvio.nascimento@gmail.com")
pyautogui.press("tab")
pyautogui.write("silvio123456")
pyautogui.press("tab")
pyautogui.press("enter")

# cadastrar cada produto da tabela
for linha in produtos.index:
    pyautogui.click(x=437, y=292) 
    pyautogui.write(str(produtos.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(produtos.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(produtos.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(produtos.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(produtos.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(produtos.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    if str(produtos.loc[linha, "obs"]).lower() != "nan":
        pyautogui.write(str(produtos.loc[linha, "obs"]))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(10000)
