#---------------------
# numeros primos
# Autor: Jose Carlos
#---------------------

escolha = input('1 - para verificar se um numero e primo \n2 - verificar todos os primos ate um determonado número \n>>>')

if (escolha == '1'):
    n = int(input('Digite um numero: '))
    x = int
    k = False
    i = 2

    if (n <= 1 or n % 2 == 0):
        print('Informe um valor maior que 1 e impar')
    else:
        while k is False:
            x = n % (i)
            print ('Estou dividindo por: ', i)
            if i > (n/2):
                print('e primo')
                k = True
            if x == 0:
                print ('Nao e primo, pois e div por: ', i)
                k = True
            else:    
                 i +=1
elif (escolha == '2'):
    primeira = 's'
    i = 3
    n = int(input('Digite um número '))
    k = 5
    if (n <= 5):
        print('Informe um valor maior que 5!')
    else:
        while (k <= n):
            primo = False
            while primo == False:
                x = k % i
                if (x == 0):
                    i = 3
                    k +=2
                    primo = True
                    #break
                else:
                    i +=2
                    if (i >= k/2):
                        #break
                        primo = True
                        if (primeira == 's'):
                            print ('2 é um primo')
                            print ('3 é um primo')
                            primeira = 'n'
                        print (k, 'é um primo')
                        i = 3
                        k +=2
    input()                    
else:
    print (escolha, 'não é uma opcao válida!')
