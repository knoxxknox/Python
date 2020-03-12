# Meu ID 851842816

import telepot
import pyrebase

token = '938468576:AAEDCnGVdYpFim4zJ-IApXlJD5hqDGQ5PL8'
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
    indice = dados.child("Pessoas").child(id).child("indice")get()
    if (indice.val() == None or int(indice.val) == 30):
        dados.child("Pessoas").child(id).update({"indice":"1"})
        indice = 1
    arq = pend + text + indice + ".JPG"    
    caminho = ("/home/pi/Desktop/projetoProf/" + pend + "/" + text + "/" + arq)
    bot.sendPhoto(id, open(caminho, 'rb'), "Segue sua solicitação")
    novoIndice = int(indice.val()) + 1
    dados.child("Pessoas").child(id).update({"indice":novoIndice})

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
            bot.sendMessage(id, ('Olá ' + fNome + ', você ainda não está cadastrado por aqui. Por favor, envie CADASTRAR para prosseguir.'))
        else:
            cad(id, fNome, lNome) #Cadsatro de usuário após validação de existência
    else:
        prosseguir = True

    if text == 'MENU':
        prosseguir = False
        bot.sendMessage(id, (fNome + ' menu.'))

    if prosseguir == True:
        pend = (verifPend(id)) #funçao trás retorno, instrução return
        if pend != None:
            if (text == 'A' or text == 'B' or text == 'C' or text == 'D' or text == 'E' or text == 'F'):     
                enviaConteudo(pend, text, id)        
            if text == 'SAIR':
                bot.sendMessage(id, (fNome + ' você desativou o envio do conteúdo do ' + pend + ' ano, caso deseje digite MENU para recomeçar.'))
                dados.child("Pessoas").child(id).child("pend").remove()
            else:
                bot.sendMessage(id, (fNome + ', como atualmente você está com o conteúdo do ' + pend + ' ano aberto, você pode fecha-lo para então escolher outro diretório enviado SAIR, ou utilizar um dos comando abixo para o ' + pend + ' ano.'))
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
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento SAIR para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'))
                conteudo6Ano(id)
            elif text == '7':
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento SAIR para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'))
                conteudo7Ano(id)
            elif text == '8':  
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento SAIR para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'))
                conteudo8Ano(id)  
            elif text == '9':  
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento SAIR para fecha-lo, ou envie um dos comandos abaixo para receber o conteúdo.'))
                conteudo9Ano(id) 
            else:
                bot.sendMessage(id, (fNome + ' você digitou um comando inválido. Digite MENU e veja como prosseguir.'))

bot = telepot.Bot(token)
bot.message_loop(receber)
while True:
    pass
#185155612923