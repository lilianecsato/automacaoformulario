import pyautogui
import time

# pyautogui.pause -> serve para definir um tempo de espera
# entre cada comando do pyautogui
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome  
# (Os comandos abaixo 1° irá abrir a janela do Windows e depois o Chrome)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Para fazer o Login teremos que usar o time que é uma biblioteca.
# pyautogui.pause adiciona uma pausa automática entre comandos do PyAutoGUI,
# enquanto time.sleep() pausa a execução do programa manualmente por um tempo definido.

# Importar a biblioteca e Esperar 3 segundos
time.sleep(3)

#Passo 2: Fazer o Login 
#Preencher o e-mail
#O print(pyautogui.position() está no arquivo auxiliar
pyautogui.click(x=465, y=725)
pyautogui.write("pythonimpressionador@gmail.com")

#Preencher a senha
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")

#botão logar
pyautogui.press("tab")
pyautogui.press("enter")

#Espera de 3 segundos
time.sleep(3)

#Passo 3: Importar a base de Dados
""" Para importar os dados, temos que ter o arquivo .csv e importar o Pandas. Abra o terminal e digite: pip install pandas """
import pandas

pandas.read_csv("produtos.csv")

"""Vamos aramazenar essa base de dados em uma "caixinha" que no caso aqui será o nome de Tabela"""
tabela = pandas.read_csv("produtos.csv")

# O print irá printar no terminal toda a tabela 
print(tabela)

# Passo 4 Cadastrar um produto

for linha in tabela.index:#para cada linha da minha tabela
    pyautogui.click(x=884, y=515)


    #codigo = "MOLO000251"
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") #passar para o próximo campo
    #marca = "Logitech"
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)      
    

    pyautogui.press("tab") #passar para o próximo campo
    tipo = "mouse"
    pyautogui.write(tipo)

    pyautogui.press("tab") #passar para o próximo campo
    categoria = "1"
    pyautogui.write(categoria)

    pyautogui.press("tab") #passar para o próximo campo
    preco_unitario = "25.95"
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") #passar para o próximo campo
    custo = "6.50"
    pyautogui.write(custo)

    pyautogui.press("tab") #passar para o próximo campo
    obs = ""
    pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(100000)


#Passo 5, repetir para todos os produtos colocando um for no passo 4















