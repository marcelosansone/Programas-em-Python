c0 = int (input('Numero inteiro nao nulo natural:'))
i=0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        i += 1
        print (c0)
    elif c0 % 2 == 1:
        c0 = c0 * 3 + 1
        i += 1
        print (c0)
else:
    print ("Número de passos: ", i)    