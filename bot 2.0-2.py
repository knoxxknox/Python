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

# ===================================================================================
# ------------------- Bloco de definição de funções do bot --------------------------
# ===================================================================================

def cad(id, fNome, lNome): # Função para cadastro de usuário no BD firebase

    inf = [{"fist_name":fNome,
            "last_name":lNome
            }
          ]

    for elemento in inf:
        nome = elemento['fist_name']
        dados.child("Pessoas").child(id).update(elemento)
        
    bot.sendMessage(id, ('Cadastrado realizado com sucesso!'))
    
def verifPend(id):
    user = dados.child("Pessoas").child(id).child("pend").get()
    return(user.val())
 
def menu(id):
    msg = 'Menu em construção!!'
    bot.sendMessage(id, msg)

# ===================================================================================
# ------------------- Bloco de definição de funções do bot --------------------------
# ===================================================================================

def receber(msg):  # Recebe dados do robô 
    text = (msg['text']).upper()
    id = msg['from']['id']
    fNome = msg['from']['first_name']
    lNome = msg['from']['last_name']
    prosseguir = False
    
    # Consultado o BD pelo get para verificar a existência do ID
    user = dados.child("Pessoas").child(id).get()
    if user.val() == None:
        if text != 'CADASTRAR':
            bot.sendMessage(id, ('Olá ' + fNome + ', você não possui cadastro. Envie CADASTRAR'))
        else:
            cad(id, fNome, lNome) #Cadsatro de usuário após validação de existência
    else:
        prosseguir = True
    
    if prosseguir == True:
        pend = (verifPend(id)) #funçao trás retorno, instrução return
        if pend != None:
            if pend == 'email':
                temArroba = True if '@' in text else False
                temPtCom = True if '.COM' in text else False
                if ((temArroba == True) and (temPtCom == True)):
                    text = text.lower()
                    dados.child("Pessoas").child(id).child("pend").remove()
                    dados.child("Pessoas").child(id).update({"e-mail":text})
                    bot.sendMessage(id, ('Seu e-mail foi cadastrado com sucesso!'))
                else:
                    bot.sendMessage(id, ('Por favor digite um e-mail válido para cadastramento'))
        else:
            print('sem pendencia')
            if text == 'EMAIL':
                dados.child("Pessoas").child(id).update({"pend":"email"})
                bot.sendMessage(id, ('Ok, agora digite um e-mail válido para cadastramento'))
                
            if text == 'MENU':
               menu(id) 
           
bot = telepot.Bot(token)
bot.message_loop(receber)
while True:
    pass
#185155612923