# Alertar e pedir informações no PyAutoGUI

import pyautogui

# #pyautogui.alert(text='Iniciando sua automação',title='Automação de Login',button='ok')

# # Pedir informção
# # email = pyautogui.prompt(text='Digite seu e-mail',title='informações obrigatórias')
# # print(f'você digitou {email}')
# # Confirmar se algo deve ou não acontecer

# resposta = pyautogui.confirm(text='Continuar rodando nossa automção?',title='confirmação',buttons=['sim','não','cancelar'])

# # print(resposta)

# if resposta == 'sim':
#     print('continuando automção')
# elif resposta == 'não':
#     print('encerrando automação')
# else:
#     print('operação cancelada')

#senha = pyautogui.password(text='digite sua senha:',title='dados de login',mask='*')
#print(senha)

# DESAFIO COLETAR EMAIL E SENHA COLAR NO BLOCO DE NOTAS
email = pyautogui.prompt(text='Digite seu e-mail',title='Dados de Login')
senha = pyautogui.password(text='Digite sua senha:',title='dados de login',mask='*')

pyautogui.click(176,423,duration=2)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)