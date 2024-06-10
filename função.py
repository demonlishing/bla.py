import random


def apresentarpalavra(letras, palavra):
    npalavra = "_ " * len(palavra)
    for x in range(0 , len(letras)):
        #print(letras[x])
        for p in range(0 , len(palavra)):      
            #print(palavra[p])
            if letras[x]== palavra[p]:
                npalavra = npalavra[0:p*2] + palavra[p] + "_ " + npalavra[p*2: ]
                print(letras[x])
    return npalavra

print(apresentarpalavra("ABx" , "Amor"))
