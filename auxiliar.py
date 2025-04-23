import pyautogui
import time

""" Aqui vamos rodar o código, usar `sleep`
    para aguardar 5 segundos e dar tempo do
    print(pyautogui.position())` exibirá a posição atual do cursor."""
time.sleep(5)

"""Simula a rolagem do mouse:
pyautogui.scroll(300) → rola para cima
pyautogui.scroll(-300) → rola para baixo
Use para navegar por páginas, listas ou telas longas automaticamente.
"""
pyautogui.scroll(100000)  

"""O print(pyautogui.position())
    serve para exibir no terminal 
    as coordenadas atuais do cursor
    do mouse na tela."""
print(pyautogui.position())



  




