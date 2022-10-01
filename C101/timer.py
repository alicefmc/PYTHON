import time


segundos = float(input("digite o tempo, em segundos"))

def contagem_regressiva(segundos):
    while segundos > 0:
        minutos = int(segundos/60)
        seg = int(segundos%60)
        tempo = f"{minutos}:{seg}"
        print (tempo,end="\r")
        time.sleep(1)
        segundos -= 1
    print ("tempo esgotado")
    
    
contagem_regressiva(int(segundos))    