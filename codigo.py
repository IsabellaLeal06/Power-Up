# importando as bibliotecas
import pyautogui 
import time
import pandas as pd

# criando variável 'link', onde será armazenado o link do site

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


pyautogui.PAUSE = 0.7 # pausa para cada ação que a IA realizar 
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter") 

time.sleep(3) # espera 3 segundos para poder realizar a próxima ação

pyautogui.write(link)
pyautogui.press("enter") 

time.sleep(3) # espera 3 segundos para poder realizar a próxima ação

pyautogui.click(x=691, y=374) 
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") 
pyautogui.write("senha segura") 
pyautogui.press("enter") 

time.sleep(3)

tabela = pd.read_csv("produtos.csv") 
print(tabela)

for linha in tabela.index:
    
    pyautogui.click( x=687, y=257) # clica no primeiro input
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(str(codigo)) # escrever
    pyautogui.press("tab") # próximo
    
    # marca
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

    
    # obs
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)