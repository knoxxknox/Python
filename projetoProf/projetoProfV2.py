# Meu ID 851842816

import pyrebase
import random
import time
import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

token = '1009820696:AAE_GTTncwmgj3aVaikS-InZ8N-OUDK3nNE'
config = {
    "apiKey":"AIzaSyD_Y8Lm4XdB3xZtASOGuWA9sN1RCMRzgB0",
    "authDomain":"knoxpi.firebaseapp.com",
    "databaseURL":"https://knoxpi.firebaseio.com",
    "projectId":"knoxpi",
    "storageBucket":"knoxpi.appspot.com",
    "messagingSenderId":"126266786859",
    "appId":"1:126266786859:web:360328bba2a48b98e8966e",
    "measurementId":"G-QZ6KRS35Z8"
}

firebase = pyrebase.initialize_app(config)
dados = firebase.database()

# --------------------------------------------
# Bloco de denifição de funcoes auxiliáres
# --------------------------------------------

def cad(id, fNome, lNome): # Função para cadastro de usuário no BD firebase
    inf = [{"fist_name":fNome,
            "last_name":lNome
            }
          ]
    
    for elemento in inf:
        #nome = elemento['fist_name']
        dados.child("Pessoas").child(id).update(elemento)        
    bot.sendMessage(id, (fNome + ' seu cadastrado realizado com sucesso!'))
    time.sleep(3)
    msg = ""
    arquivo = open('/home/pi/Desktop/projetoProf/cadastro.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = msg + linha + '\n'
    bot.sendMessage(id, msg, parse_mode= 'Markdown')    
    arquivo.close()
    

def cadBotao(from_id): # Função para cadastro de usuário no BD firebase
    dados.child("Pessoas").child(from_id).update({"fist_name":"ALGUEM"})
    bot.sendMessage(from_id, ('Seu cadastrado realizado com sucesso!'))
    time.sleep(3)
    msg = ""
    arquivo = open('/home/pi/Desktop/projetoProf/cadastro.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = msg + linha + '\n'
    bot.sendMessage(from_id, msg, parse_mode= 'Markdown')    
    arquivo.close()


def verifPend(id):
    pend = dados.child("Pessoas").child(id).child("pend").get()
    
    return(pend.val())

def conteudo6Ano(id):
    msg = ''
    arquivo = open('/home/pi/Desktop/projetoProf/conteudo6Ano.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = msg + linha + '\n'
    bot.sendMessage(id, msg)    
    arquivo.close()

def conteudo7Ano(id):
    msg = ''
    arquivo = open('/home/pi/Desktop/projetoProf/conteudo7Ano.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = msg + linha + '\n'
    bot.sendMessage(id, msg)    
    arquivo.close()

def conteudo8Ano(id):
    msg = ''
    arquivo = open('/home/pi/Desktop/projetoProf/conteudo8Ano.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = msg + linha + '\n'
    bot.sendMessage(id, msg)    
    arquivo.close()       

def conteudo9Ano(id):
    msg = ''
    arquivo = open('/home/pi/Desktop/projetoProf/conteudo9Ano.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = msg + linha + '\n'
    bot.sendMessage(id, msg)    
    arquivo.close()

def enviaConteudo(pend, text, id):
    if len(text) == 1:
        indice = random.randint(1,1)
        indiceStr = str(indice)
        arq = pend + text + indiceStr + ".jpeg"    
        caminho = ("/home/pi/Desktop/projetoProf/" + pend + "/" + text + "/" + arq)
        ID = pend + text + indiceStr
        bot.sendPhoto(id, open(caminho, 'rb'), "Id - " + ID)
    else:
        arq = pend + text + ".jpeg"    
        caminho = ("/home/pi/Desktop/projetoProf/" + pend + "/" + text + "/" + arq)
        bot.sendPhoto(id, open(caminho, 'rb'), "Segue sua solicitação")
        # Não é envio de quesões e sim de informações sobre o tópico
        
def funcaoAuxiliarComPend(from_id, nome, pend):
    bot.sendMessage(from_id, (nome + ', como atualmente você está com o conteúdo do ' + pend + ' ano aberto, você pode fecha-lo para então escolher outro diretório enviado *SAIR*, ou utilizar um dos comando abixo referentes ao ' + pend + ' ano.'), parse_mode= 'Markdown')
    time.sleep(1)
    if pend == '6':
        conteudo6Ano(from_id)
    elif pend == '7':
        conteudo7Ano(from_id)
    elif pend == '8':   
        conteudo8Ano(from_id)  
    elif pend == '9':   
        conteudo9Ano(from_id) 
    
def funcaoAuxiliarSemPend(from_id, nome, query_data):
    dados.child("Pessoas").child(from_id).update({"pend":query_data})
    bot.sendMessage(from_id, (nome + ' você está dentro do diretório do ' + query_data + ' ano. Envie a qualquer momento *SAIR* para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'), parse_mode= 'Markdown')
    time.sleep(1)
    
def receberQuerry(msg):
    
    query_id, from_id, query_data  = telepot.glance(msg, flavor='callback_query')
    pend = (verifPend(from_id))
    nome = dados.child("Pessoas").child(from_id).child("fist_name").get()

    if query_data == "6":
        if pend != None:
            funcaoAuxiliarComPend(from_id,nome.val(), pend) 
        else:
            print("entrei aqui 2")
            funcaoAuxiliarSemPend(from_id, nome.val(), query_data) 
            conteudo6Ano(from_id)

    if query_data == "7":
        if pend != None: 
            funcaoAuxiliarComPend(from_id, nome.val(), pend)
        else:    
            funcaoAuxiliarSemPend(from_id, nome, query_data) 
            conteudo7Ano(from_id)
                 
    if query_data == "8":
        if pend != None:
            funcaoAuxiliarComPend(from_id, nome.val(), pend)
        else:   
            funcaoAuxiliarSemPend(from_id, nome.val(), query_data) 
            conteudo8Ano(from_id) 
        
    if query_data == "9":
        if pend != None:
            funcaoAuxiliarComPend(from_id, nome.val(), pend)
        else:
            funcaoAuxiliarSemPend(from_id, nome.val(), query_data) 
            conteudo7Ano(from_id)
             
    if query_data == "CADASTRAR":
        cadBotao(from_id)
    elif (query_data == 'A' or query_data == 'B' or query_data == 'C' or query_data == 'D' or query_data == 'E' or query_data == 'F'):
        if pend == None:
            bot.sendMessage(from_id, ('Você não possui nenhum diretório aberto. Digite *MENU* e veja como prosseguir.'), parse_mode= 'Markdown')
        else:   
            enviaConteudo(pend, query_data, from_id)     


# -------------------------------------------------
# Inicio do processo com captura de dados pelo robô
# -------------------------------------------------

def receber(msg): 
    text = (msg['text']).upper()
    id = msg['from']['id']
    fNome = msg['from']['first_name']
    lNome = msg['from']['last_name']
    prosseguir = False
    
    # Consultado o BD pelo get para verificar a existência do ID
    user = dados.child("Pessoas").child(id).get()
    if user.val() == None:
        if text != 'CADASTRAR':  
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                           [InlineKeyboardButton(text='Iniciar o cadastro', callback_data='CADASTRAR')],
                       ])
            bot.sendMessage(id, ('Olá ' + fNome + ', você ainda não está cadastrado por aqui. Por favor, envie CADASTRAR ou precione o botão abaixo para prosseguir.'), reply_markup=keyboard)        
        else:
            cad(id, fNome, lNome) #Cadsatro de usuário após validação de existência
    else:
        prosseguir = True      
        nome = dados.child("Pessoas").child(id).child("fist_name").get()
        if nome.val() == "ALGUEM":
            inf = [{"fist_name":fNome,
                    "last_name":lNome
                    }
                  ]
            for elemento in inf:
                dados.child("Pessoas").child(id).update(elemento)               
    if text == 'MENU':
        prosseguir = False
        msg = ""
        arquivo = open('/home/pi/Desktop/projetoProf/menu.txt','r')
        for linha in arquivo:
            linha = linha.rstrip()
            msg = msg + linha + '\n'
        bot.sendMessage(id, msg, parse_mode= 'Markdown')    
        arquivo.close()

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                       [InlineKeyboardButton(text='6 ano', callback_data='6')],[InlineKeyboardButton(text='7 ano', callback_data='7')],
                       [InlineKeyboardButton(text='8 ano', callback_data='8')],[InlineKeyboardButton(text='9 ano', callback_data='9')],
                   ])
        bot.sendMessage(id, 'Selecione abaixo sua opção', reply_markup=keyboard)
        
    if text == 'SOBRE':
        prosseguir = False
        msg = ""
        arquivo = open('/home/pi/Desktop/projetoProf/sobre.txt','r')
        for linha in arquivo:
            linha = linha.rstrip()
            msg = msg + linha + '\n'
        bot.sendMessage(id, msg, parse_mode= 'Markdown')    
        arquivo.close()
    
    if prosseguir == True:
        pend = (verifPend(id)) #funçao trás retorno, instrução return
        if pend != None:
            if (text == 'A' or text == 'B' or text == 'C' or text == 'D' or text == 'E' or text == 'F'):     
                enviaConteudo(pend, text, id)        
            elif text == 'SAIR':
                bot.sendMessage(id, (fNome + ' você desativou o envio do conteúdo do ' + pend + ' ano, caso deseje digite *MENU* para recomeçar.'), parse_mode= 'Markdown')
                dados.child("Pessoas").child(id).child("pend").remove()
            else:
                bot.sendMessage(id, (fNome + ', como atualmente você está com o conteúdo do ' + pend + ' ano aberto, você pode fecha-lo para então escolher outro diretório enviado *SAIR*, ou utilizar um dos comando abixo referentes ao ' + pend + ' ano.'), parse_mode= 'Markdown')
                time.sleep(1)
                if pend == '6':
                    conteudo6Ano(id)
                elif pend == '7':
                    conteudo7Ano(id)
                elif pend == '8':   
                    conteudo8Ano(id)  
                elif pend == '9':   
                    conteudo9Ano(id)                    
        else:     
            if text == '6':
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento *SAIR* para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'), parse_mode= 'Markdown')
                time.sleep(1)
                conteudo6Ano(id)
            elif text == '7':
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento *SAIR* para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'), parse_mode= 'Markdown')
                time.sleep(1)
                conteudo7Ano(id)
            elif text == '8':  
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento *SAIR* para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'), parse_mode= 'Markdown')
                time.sleep(1)
                conteudo8Ano(id)  
            elif text == '9':  
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento *SAIR* para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'), parse_mode= 'Markdown')
                time.sleep(1)
                conteudo9Ano(id) 
            else:
                bot.sendMessage(id, (fNome + ' você não possui nenhum diretório aberto. Digite *MENU* e veja como prosseguir.'), parse_mode= 'Markdown')


bot = telepot.Bot(token)
MessageLoop(bot, {'chat': receber,
                  'callback_query': receberQuerry}).run_as_thread()

while 1:
    time.sleep(10)


'''
bot = telepot.Bot(token)
bot.message_loop(receber)
while True:
    pass
#185155612923
'''