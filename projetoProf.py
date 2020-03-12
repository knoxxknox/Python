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
    arquivo = open('/Users/knox/Desktop/conteudo6Ano.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        msg = linha
    arquivo.close()
    print (linha)
    bot.sendMessage(id, 'teste')

def conteudo7Ano(id):
    print ('aaa')

def conteudo8Ano(id):
    print ('aaa')        

def conteudo9Ano(id):
    print ('aaa')

# -------------------------------------------------
# Inicio do processo com captura de dados no robô
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
            if pend == '6' or pend == '7' or pend == '8' or pend == '9':
                if (text == 'A' or text == 'B' or text == 'C' or text == 'D' or text == 'E' or text == 'F'):     
                    print ('aaaaa')
                    # ENVIAR ARQUIVO LENDO O DIRETORIO CORRETO
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
            if text == '6' or text == '7' or text == '8' or text == '9':
                dados.child("Pessoas").child(id).update({"pend":text})
                bot.sendMessage(id, (fNome + ' você está dentro do diretório do ' + text + ' ano. Envie a qualquer momento SAIR para fecha-lo, ou um dos comandos abaixo para receber o conteúdo.'))
                if text == '6':
                    conteudo6Ano(id)
                elif text == '7':
                    conteudo7Ano(id)
                elif text == '8':   
                    conteudo8Ano(id)  
                elif text == '9':   
                    conteudo9Ano(id)    
            else:
                bot.sendMessage(id, (fNome + ' você digitou um comando inválido. Digite MENU e veja como prosseguir.'))

bot = telepot.Bot(token)
bot.message_loop(receber)
while True:
    pass
#185155612923


'''
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

'''