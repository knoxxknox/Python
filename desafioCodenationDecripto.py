
# Decodificador para desafio Codenation - José Carlos

textoCifrado = "abcf.12a"
chave = 1
tamTextoCifrado = len(textoCifrado)

abc1 = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
abc1Recuperar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abcIndiceNegativo = {-1:"z", -2:"y", -3:"x", -4:"w", -5:"v", -6:"u", -7:"t", -8:"s", -9:"r", -10:"q", -11:"p", -12:"o", -13:"n", -14:"m", -15:"l", -16:"k", -17:"j", -18:"i", -19:"h", -20:"g", -21:"f", -22:"e", -23:"d", -24:"c", -25:"b"}

n = 0
while n <= tamTextoCifrado:
    if n >= tamTextoCifrado:
        break
    letra = textoCifrado[n]
    valido = False
    for testeExcecao in abc1Recuperar:
        if testeExcecao == letra:
            valido = True
            break
    if valido == True:
        indiceDeLetra = abc1.get(letra)
        indice = indiceDeLetra - chave
        
        if indice >= 0:
            letraDecifrada = abc1Recuperar[indice]
            print(letraDecifrada)
        else:
            letraDecifrada = abcIndiceNegativo.get(indice)
            print(letraDecifrada)
    else:
          print(letra)  
    n +=1