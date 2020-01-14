'''
Le arquivo TXT contendo ID, Token e nomeArq.jpg para envio de imagens JPG pelo Telegram.
Autor: José Carlos
Data: 07/01/2020

token = '938468576:AAEDCnGVdYpFim4zJ-IApXlJD5hqDGQ5PL8'
Meu ID 851842816
'''

import telepot
from datetime import date

# Lendo o arquivo TXT para capturar os parâmetros necessários 
dadosArray = []
arquivo = open('C:\SCHEDULE\ARQUIVOS-PYTHON\parmPython.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    dadosArray.append(linha) # Gravando conteúdo TXT na array
arquivo.close()

# Recuperando dados do TXT salvos no array
token = dadosArray[0]
id = dadosArray[1]

bot = telepot.Bot(token)

arqPrint = dadosArray[2:len(dadosArray)] #contem nomes dos aqruivos a serem enviados

for arq in arqPrint:
    caminho = ('C:\SCHEDULE\ARQUIVOS-PYTHON') + arq
    bot.sendPhoto(id, open(caminho, 'rb'), "Segue sua solicitação...")   

