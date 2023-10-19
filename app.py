from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
pyautogui.click(620,164)

