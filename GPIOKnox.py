import RPi.GPIO as GPIO
import time
import telepot

token = '938468576:AAEDCnGVdYpFim4zJ-IApXlJD5hqDGQ5PL8'
bot = telepot.Bot(token)

GPIO.setmode(GPIO.BOARD)
TRIGGER = 11
ECHO = 12

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
time.sleep(1)

try:
    while(True):
        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)
        
        while GPIO.input(ECHO) == 0:
            tempo_inicial = time.time()
            
        while GPIO.input(ECHO) == 1:
            tempo_final = time.time()
            
        tempo_total = tempo_final - tempo_inicial
        distancia = (tempo_total * 34000)/2
        time.sleep(0.1)
        #print(round(distancia, 3) , ' cm')
        if distancia < 10:
            print ('PERIGO!!!')
            bot.sendMessage(851842816, 'ALGUEM SE APROXIMOU')
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
            
            
            