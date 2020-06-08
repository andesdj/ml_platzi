# -*- coding: utf-8 -*-

def isprime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n<2 and n %2==0:
        return False
    else:
        for i in range(3,n):
            if n%i==0:
                return False
    return True
    

def run ():
    num=int(input('Ingrese un numero:..'))
    r=isprime(num)
    
    if r is True:
        m='Tu numero  es primo ',num
    else:
        m='Tu numero  no es primo ',num

    print(m)
if __name__ =='__main__':
    run()

