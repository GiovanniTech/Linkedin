import time
import pyautogui

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyautogui.sleep(2)
pyautogui.write("https://www.linkedin.com/feed/")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(511,103)
pyautogui.write("Programador Python")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(620,164)
time.sleep(2)
pyautogui.click(1130,395)
time.sleep(2)
pyautogui.click(1017,300)
time.sleep(2)
pyautogui.write("Ola, estou comecando na area de programacao utilizando a linguagem Python e seria de grande utilidade conectar com voce que também opera com esta linguagem, essa e uma automacao utilizando Pyautogui, se recebeu essa mensagem, essa automacao funcionou; Vamos construir uma rede e aprender juntos! 😊")
time.sleep(6)
pyautogui.click(1020,164)

# Note que você deve alterar os " pyautogui.click " de acordo com eixo X and Y da sua tela.
# Você pode utilizar o comando dentro do CMD para printar onde seu mouse estiver, o comando é "python -m mouseinfo"
# Caso não tenha instalado, utilize " pip install mouseinfo"