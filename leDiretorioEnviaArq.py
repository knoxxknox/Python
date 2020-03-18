import os, telepot

token = '1009820696:AAE_GTTncwmgj3aVaikS-InZ8N-OUDK3nNE'

def geraTupla():
    caminho = "/home/pi/Desktop/d" 
    for _, _, arquivo in os.walk(caminho):
        return(arquivo)    

def receber(msg): 
    text = (msg['text']).upper()
    id = msg['from']['id']
    fNome = msg['from']['first_name']
    lNome = msg['from']['last_name']

    if text == "LISTAR":
        arq = ""
        caminho = "/home/pi/Desktop/d"
        indice = 0

        for _, _, arquivo in os.walk(caminho):
            for item in arquivo:
                arq = arq + str(indice) + "-" + item + "\n"
                indice += 1  
            bot.sendMessage(id, ('Olá ' + fNome + ', segue a lista de arquivos na pasta: \n\n' + arq))
    else:
        arquivo = geraTupla()
        indiceEscolhido = int(text)
        maximo = len(arquivo)
        if indiceEscolhido > maximo:
            bot.sendMessage(id, (fNome + ', esse arquivo não existe!') )
        else:
            caminho = "/home/pi/Desktop/d" 
            arqEscolhido = arquivo[indiceEscolhido]
            enviarArquivo = caminho + "/" + arqEscolhido
            bot.sendPhoto(id, open(enviarArquivo, 'rb'), ";)")
          
bot = telepot.Bot(token)
bot.message_loop(receber)
while True:
    pass
