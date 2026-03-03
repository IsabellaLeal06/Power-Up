# importando as bibliotecas
import pyautogui 
import time

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