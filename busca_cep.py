'''
Autor .....: José Carlos C. Augusto
Data ......: 2020-07-16
Descrição .: Recebe solicitação via Telegram e realiza consulta de CPE no banco Mysql
             devolvendo ao solicitante os dados da consulta
'''

import telepot
import mysql.connector


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="raspberry",
    database="KNOX"
)

cursor = banco.cursor()
token = '1009820696:AAE_GTTncwmgj3aVaikS-InZ8N-OUDK3nNE'
bot = telepot.Bot(token)

def pesquisa_sql(id, text):
    comando_SQL = "SELECT * FROM ceps2 WHERE cep = " + text
    cursor.execute(comando_SQL)
    retorno_consulta = cursor.fetchall()
    if len(retorno_consulta) > 0: 
        if retorno_consulta[0][5] != " ":
            msg = (
                "\nMunicipio = " + retorno_consulta[0][2] +
                "\nBairro = " + retorno_consulta[0][3] +
                "\nLogradouro = " + retorno_consulta[0][4] +
                "\nComplemento = " + retorno_consulta[0][5]
            )
        else:
            msg = (
                "\nMunicipio = " + retorno_consulta[0][2] +
                "\nBairro = " + retorno_consulta[0][3] +
                "\nLogradouro = " + retorno_consulta[0][4]
            )
        
        bot.sendMessage(id, msg)
    else:
        bot.sendMessage(id, "Sem resultados para o CEP " + text)

def receber(msg):
    text = (msg['text']).upper()
    id = msg['from']['id']
    fNome = msg['from']['first_name']
    if text.isdigit() is True:
        pesquisa_sql(id,text)
    else:    
        bot.sendMessage(id, (fNome + ", apenas valores numéricos são aceitos"))

bot.message_loop(receber)
while True:
    pass
