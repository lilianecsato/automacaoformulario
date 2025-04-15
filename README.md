# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2: Fazer o login
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 Produto
# Passo 5: Repetir para todos os produtos

# Biblioteca: Instalar um pacote para fazer automações com python (pyautogui)
# clicar no terminal  e digitar: pip install pyautogui e aguardar a instalação caso já não tenha instalado.

# O import pyautogui serve para automatizar o controle do mouse e do teclado em Python, permitindo interações com a interface gráfica do usuário.

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas
# pyautogui.pause -> serve para definir um tempo de espera 


O `pyautogui.pause` serve para **definir um tempo de espera automático entre cada comando do PyAutoGUI**. Isso é útil para deixar a automação mais lenta e estável, evitando que os comandos sejam executados rápido demais.

### Exemplo:
```python
import pyautogui

pyautogui.pause = 1  # Espera 1 segundo após cada comando

pyautogui.moveTo(100, 100)
pyautogui.click()
```

Nesse exemplo, o PyAutoGUI vai esperar 1 segundo **depois de mover o mouse** e mais 1 segundo **depois de clicar**.

👉 Útil para depuração ou para dar tempo ao sistema/processos entre ações.

"""Para não precisar usar o O print(pyautogui.position(),
vamos usar o tab, assim a após digitar o e-mailé só apertar o 
tab automaticamente que irá para o próximo campo"""

#Passo 3: Importar a base de Dados
""" Para importar os dados, temos que ter o arquivo .csv e importar o Pandas. Abra o terminal e digite: pip install pandas """

"""Vamos aramazenar essa base de dados pandas.read_csv("produtos.csv") em uma "caixinha" que no caso aqui será o nome de Tabela"""


# O print irá printar no terminal toda a tabela 
print(tabela)

