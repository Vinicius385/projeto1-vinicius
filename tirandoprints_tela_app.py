# Como tirar print(foto) da tela inteira ou parte dela 
import pyautogui
import pyscreeze
# Tirar print da tela inteira
#pyautogui.screenshot('tela.jpg')
# Tirar um print de parte da tela 
pyautogui.screenshot('calculadora.jpg',region=(256,289,400,400))