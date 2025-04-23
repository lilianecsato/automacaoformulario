# Importa a biblioteca pyautogui, usada para automação de mouse e teclado
import pyautogui
# Importa a biblioteca time, usada para adicionar pausas (delays) no código
import time
# Importa a biblioteca pandas, usada para manipulação de arquivos e dados (como o CSV)
import pandas

# Define um tempo de pausa de 0.5 segundos entre cada comando do pyautogui
pyautogui.PAUSE = 0.5

# Pressiona a tecla "Windows" para abrir o menu iniciar
pyautogui.press("win")
# Digita "chrome" para buscar o navegador
pyautogui.write("chrome")
# Pressiona Enter para abrir o navegador Google Chrome
pyautogui.press("enter")

# Digita o link do sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# Pressiona Enter para acessar o site
pyautogui.press("enter")

# Aguarda 3 segundos para garantir que o site carregue
time.sleep(3)

# Clica na posição do campo de e-mail (posição precisa ser coletada com pyautogui.position())
pyautogui.click(x=465, y=725)
# Digita o e-mail de login
pyautogui.write("pythonimpressionador@gmail.com")
# Pressiona TAB para ir para o campo da senha
pyautogui.press("tab")
# Digita a senha
pyautogui.write("minhasenhasupersecreta")
# Pressiona TAB para ir até o botão "Logar"
pyautogui.press("tab")
# Pressiona Enter para realizar o login
pyautogui.press("enter")

# Aguarda 3 segundos para o sistema carregar após o login
time.sleep(3)

# Lê o arquivo CSV chamado "produtos.csv" (a primeira leitura é opcional aqui)
pandas.read_csv("produtos.csv")
# Lê novamente e armazena a base de dados na variável "tabela"
tabela = pandas.read_csv("produtos.csv")
# Exibe a tabela no terminal para ver os dados importados
print(tabela)

# Clica na posição do botão de cadastro de produto (posição coletada previamente)
pyautogui.click(x=884, y=515)

# Define o código do produto
codigo = "MOLO000251"
# Digita o código
pyautogui.write(codigo)
# Passa para o próximo campo
pyautogui.press("tab")

# Define a marca
marca = "Logitech"
# Digita a marca
pyautogui.write(marca)
# Próximo campo
pyautogui.press("tab")

# Define o tipo do produto
tipo = "mouse"
# Digita o tipo
pyautogui.write(tipo)
# Próximo campo
pyautogui.press("tab")

# Define a categoria
categoria = "1"
# Digita a categoria
pyautogui.write(categoria)
# Próximo campo
pyautogui.press("tab")

# Define o preço unitário
preco_unitario = "25.95"
# Digita o preço unitário
pyautogui.write(preco_unitario)
# Próximo campo
pyautogui.press("tab")

# Define o custo do produto
custo = "6.50"
# Digita o custo
pyautogui.write(custo)
# Próximo campo
pyautogui.press("tab")

# Observações (nesse caso está vazio)
obs = ""
# Digita o campo de observações
pyautogui.write(obs)

# Pressiona tab para ir até o botão de "Cadastrar"
pyautogui.press("tab")
# Pressiona enter para finalizar o cadastro
pyautogui.press("enter")

Continua ...


#Passo 5, repetir para todos os produtos colocando um for no passo 4
Para o For reconhecer, selecionar todo o passo 4 e apertar o Tab, para acontecer a "identação"