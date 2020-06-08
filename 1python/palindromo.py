# -*- coding: utf-8 -*-

def palin2(w):
    rw=w[::-1]
    if rw==w:
        return True
    return False

def palin(w):
    rever=[]
    
    for l in w:
        rever.insert(0, l)
    
    reverw=''.join(rever)
    print('Palabra ins',w)
    print('palabra Rev ',reverw)
    if w==reverw:
        return True
    else:
        return False
        
    

if __name__ =='__main__':
    word=str(input('Escribe una palabra: '))
    #res= palin(word)
    res2=palin2(word)
    if res2 is True:
        print("La palabra {} es palindroma".format(word))
    else:
        print("La palabra {} no es IGUAL".format(word))