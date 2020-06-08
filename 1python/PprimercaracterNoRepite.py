# -*- coding: utf-8 -*-


def primero_sin_r(ch):
    sl={}
    
    for idx, letter in enumerate(ch):
        if letter not in sl:
            sl[letter]=(idx,1)
        else:
            sl[letter]=(sl[letter][0], sl[letter][1]+1)
            
    fl=[]
    for key,value in sl.items():
        if value[1]==1:
            fl.append(  (key, value[0]) )
    
    not_rp = sorted(fl,key=lambda value: value[1])        
    
    if not_rp:
        return not_rp[0][0]
    else:
        return '_'
    


if __name__ =='__main__':
    char=str(input("Ingrese secuencia de caracteres: "))
    res=primero_sin_r(char)
    
    
    if res=="_":
        print("Todos los caracteres se repiten")
    else:
        print('El primer caracter no repetido es {}'.format(res))