#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:04:55 2020

@author: José Carlos C. Agusto
"""
import telepot
import time
from datetime import datetime

token = '1009820696:AAE_GTTncwmgj3aVaikS-InZ8N-OUDK3nNE'
bot = telepot.Bot(token)

def verifDiaSemana(ano, mes, dia):
    import datetime
    dt = datetime.datetime(year=ano, month=mes, day=dia)
    weekday_name = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
    wkday = dt.weekday()
    return weekday_name[wkday]

def marcaEnvioTXT(linha, linhaAlterada, diaSemana):
    arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + diaSemana + '.txt','r')
    with arquivo as fd:
        txt = fd.read()  # Ler todo o arquivo
        txt = txt.replace(linha, linhaAlterada) # Substitiu todoas as ocorrência, porém o valor é único no arquivo
        with open('/home/pi/Desktop/sistemaAlertaTelegram/' + diaSemana + '.txt','w') as fd:
            fd.write(txt)  # Escrever texto modificado

def trataLinha(linha, diaSemana):
    today = datetime.now()
    horaArquivo = int(linha[:2])
    minutoArquivo = int(linha[3:5])
    idTelegram = int(linha[6:15])
    msgEnviada = linha[16:17]
    idTXT = linha[18:23]
    status = linha[24:26]
    msg = linha[27:]

    if msgEnviada == "N" and status == "AT":
        if today.hour >= horaArquivo:
            if today.minute >= minutoArquivo:
                linhaAlterada = linha.replace("-N-", "-S-")
                marcaEnvioTXT(linha, linhaAlterada, diaSemana)
                time.sleep(1)
                bot.sendMessage(idTelegram, ("*<<ALERTA>>*\n" + msg), parse_mode= 'Markdown')

def validaMensagem(text, id, fNome):

    numero = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    diaSemana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
    critica = False
    numPrimeiro = text[:1]
    numSegundo = text[1:2]
    numTerceiro = text[3:4]
    numQuarto = text[4:5]
    week = text[6:9]
    mensagem = text[10:]
    soma = 0

    for existe in numero:
        if existe == numPrimeiro:
            soma += 1
        if existe == numSegundo:
            soma += 1
        if existe == numTerceiro:
            soma += 1
        if existe == numQuarto:
            soma += 1

    for existeSemana in diaSemana:
        if existeSemana == week:
            soma += 1

    if soma == 5:
        if (int(numPrimeiro) == 2) and (int(numSegundo) > 3):
            critica = True

        if critica == False:
                if (int(numPrimeiro) <= 2) and (int(numTerceiro) <=5):
                    # Lê a última linha do arquivo para buscar ID do TXT
                    arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + week + '.txt','r')
                    file_lines = arquivo.readlines()
                    arquivo.close()
                    last_line = file_lines[len(file_lines)-1]
                    idTXT = last_line[20:23]
                    ProxIdTXT = int(idTXT) + 1
                    tamProxIdTXT = len(str(ProxIdTXT))
                    if tamProxIdTXT == 1:
                        comp = "00"
                    elif tamProxIdTXT == 2:
                        comp = "0"
                    else:
                        comp = ""
                    conteudoEscrever = text[:5] + "-" + str(id) + "-N-id" + comp + str(ProxIdTXT) + "-AT-" + mensagem
                    arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + week + '.txt','a')
                    arquivo.write(conteudoEscrever + "\n")
                    #with openopen('/home/pi/Desktop/sistemaAlertaTelegram/' + week + '.txt','w') as fd:
                    #    fd.write(conteudoEscrever)  # Escrever texto modificado

                    arquivo.close()
                    bot.sendMessage(id, (fNome + ' seu alerta foi cadastrado com *sucesso*!\nSua mensagem será enviada todo(a) ' + week + ' às ' + text[:5]), parse_mode= 'Markdown')
                else:
                     bot.sendMessage(id, ('*ATENÇÃO: HORA E/OU MINUTO COM FORMATO INVALIDO*'), parse_mode= 'Markdown')
                     menu(id)
        else:
            bot.sendMessage(id, ('*ATENÇÃO: HORA COM FORMATO INVALIDO*'), parse_mode= 'Markdown')
            menu(id)
    else:
            bot.sendMessage(id, ('*ATENÇÃO: HORA E/OU DIA DA SEMANA INVALIDO(S)*'), parse_mode= 'Markdown')
            menu(id)

def listaMensagem(id):
    msg = ""
    diaSemana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
    for item in diaSemana:
        arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + item + '.txt','r')
        for linha in arquivo:
            linha = linha.rstrip()
            if int(linha[6:15]) == int(id) and linha[24:26] == "AT":
                msg = msg + linha[18:23] + "-" + item + "-" + linha[24:] + "\n"
        time.sleep(1)
        if len(msg) > 1:
            bot.sendMessage(id, msg)
        else:
            bot.sendMessage(id, "Você não possui alertas cadastrados para a(o) " + item)

def desativarAlerta(id, dia, idTXT, fNome):
    achou = False
    idTXT = "id" + idTXT[2:5]
    arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + dia + '.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        if linha[18:23] == idTXT and linha[6:15] == str(id):
            achou = True
            break
    if achou == True:
        hora = linha[:5]
        mensagem = linha[27:]
        linhaModif = linha.replace("AT", "HS")
        arquivo.close

        arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + dia + '.txt','r')
        with arquivo as fd:
            arqTotal = fd.read()  # Ler todo o arquivo
            arqTotal = arqTotal.replace(linha, linhaModif)
        with open('/home/pi/Desktop/sistemaAlertaTelegram/' + dia + '.txt','w') as fd:
            fd.write(arqTotal)  # Escrever texto modificado

        bot.sendMessage(id, (fNome + ", você NÃO recebera mais o alerta abaixo:"))
        bot.sendMessage(id, "*HORÁRIO:* " + hora + "\n*DIA:* " + dia + "\n*MENSAGEM:* " + mensagem, parse_mode= 'Markdown')
    else:
         bot.sendMessage(id, (fNome + " não existe alerta cadastrada para você com os dados informados.\nDigite LISTAR para verificar todos os seus alertas."))

def menu(id):
    arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/MENU.txt','r')
    with arquivo as fd:
        arqTotal = fd.read()  # Ler todo o arquivo
        bot.sendMessage(id, arqTotal)

def reload():
    diaSemana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
    for item in diaSemana:
        arquivo1 = open('/home/pi/Desktop/sistemaAlertaTelegram/' + item + '.txt','r')
        with arquivo1 as fd:
            txt = fd.read()  # Ler todo o arquivo
            txt = txt.replace("-S-", "-N-")
        with open('/home/pi/Desktop/sistemaAlertaTelegram/' + item + '.txt','w') as fd:
            fd.write(txt)  # Escrever texto modificado
        time.sleep(0.5)

def start():
    today = datetime.now()
    dia = today.day
    mes = today.month
    ano = today.year

    diaSemana = verifDiaSemana(ano, mes, dia)

    if today.hour == 0 and today.minute == 0:
        reload()
        time.sleep(60)

    arquivo = open('/home/pi/Desktop/sistemaAlertaTelegram/' + diaSemana + '.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        trataLinha(linha, diaSemana)

def receber(msg):
    text = (msg['text']).upper()
    id = msg['from']['id']
    fNome = msg['from']['first_name']
    print(text) # Desativar print
    if text == "LISTA":
        listaMensagem(id)
    elif text[:9] == "DESATIVAR":
        diaSemana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
        idTXT = text[14:19]
        validado = False
        for dia in diaSemana:
            if dia == text[10:13] and text[14:16] == "ID" and len(idTXT) == 5:
                desativarAlerta(id, dia, idTXT, fNome)
                validado = True
                break
        if validado == False:
              bot.sendMessage(id, fNome + ", informações *inválidas!*\nPara desativar um alerta envie uma mensagem no formato do exemplo a seguir:\n\n*desativar-sex-id001*\n\nCaso não saiba o id do alerta que deseja desativar, envie *LISTA* para verificar todos os seus alertas cadastrados.", parse_mode= 'Markdown')
    else:
        validaMensagem(text, id, fNome) # Valida e cadastra alerta caso esteja ok


bot = telepot.Bot(token)
bot.message_loop(receber)

while True:
    time.sleep(4)
    start()
    pass