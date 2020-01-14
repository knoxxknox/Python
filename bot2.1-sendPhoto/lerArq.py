# Lendo o arquivo criado
'''
arquivo = open('C:\SCHEDULE\ARQUIVOS-PYTHON\parmPython.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
'''

import keyboard
import string
from threading import *

"""
Optional code(extra keys):

keys.append("space_bar")
keys.append("backspace")
keys.append("shift")
keys.append("esc")
"""

# Atribuo a lista de caracteres ascii para a variavel keys(não encontrei lista com todas as teclas)
teclas = list(string.ascii_lowercase)

def listen(tecla):
    while True:
        keyboard.wait(tecla)
        print("- Tecla pressionada: ",tecla)
threads = [Thread(target=listen, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()