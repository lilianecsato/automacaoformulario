import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=465, y=725)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

pandas.read_csv("produtos.csv")
tabela = pandas.read_csv("produtos.csv")
print(tabela)

pyautogui.click(x=884, y=515)

codigo = "MOLO000251"
pyautogui.write(codigo)
pyautogui.press("tab")

marca = "Logitech"
pyautogui.write(marca)
pyautogui.press("tab")

tipo = "mouse"
pyautogui.write(tipo)
pyautogui.press("tab")

categoria = "1"
pyautogui.write(categoria)
pyautogui.press("tab")

preco_unitario = "25.95"
pyautogui.write(preco_unitario)
pyautogui.press("tab")

custo = "6.50"
pyautogui.write(custo)
pyautogui.press("tab")

obs = ""
pyautogui.write(obs)

pyautogui.press("tab")
pyautogui.press("enter")
