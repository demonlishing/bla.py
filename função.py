import random


def apresentarpalavra(letras, palavra):
    npalavra = "_ " * len(palavra)
    for x in range(0 , len(letras)):
        #print(letras[x])
        for p in range(0 , len(palavra)):      
            #print(palavra[p])
            if letras[x]== palavra[p]:
                print(letras[x])
    return npalavra

print(apresentarpalavra("ABx" , "Amor"))
