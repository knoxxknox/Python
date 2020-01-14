import pyrebase

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

# dados.update({"nome":"bob"})

# dados.child("Pessoas").child("Fulano").update({"Idade":"30"}) #navegando na estrututa

# dados.child("Pessoas").child("Fulano").remove()  #remove item do banco

# ---- Eviando dados em massa ----
'''
inf = [{"Nome":"José Carlos",
        "Idade": 31,
        "Sexo" : "M",
        "Profissão": "Analista de sistemas"},
       {"Nome":"Jéssica",
        "Idade": 27,
        "Sexo" : "F",
        "Profissão": "Professora"},
        {"Nome":"Ana",
        "Idade": 54,
        "Sexo" : "F",
        "Profissão": "Cientista"},
        {"Nome":"Fulano",
        "Idade": 542,
        "Sexo" : "M",
        "Profissão": "N/A"}
        ]

for elemento in inf:
    nome = elemento['Nome']
    dados.child("Pessoas").child(nome).update(elemento)
'''

# ---- Eviando dados subistituindo toda a estrutura por essa, novos dados----
'''
inf = {"teste/Jéssica/":{
        "Idade":28},
      "teste/Ana/":{
        "Profissão":"Criptógrafa"}
      }
dados.update(inf)
'''

# Armazena em variável dados que estáo no banco >>> comando .val <<<

'''
pessoas = dados.child("Pessoas").child("Jéssica").child("Idade").get()
print(pessoas.val())
'''

user = dados.child("Pessoas").child(8518428160).get()
if (user.val()) == None:
    print('deu certo')
















