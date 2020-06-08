# -*- coding: utf-8 -*-

def factorial(n):
    if n==0:
        return 1
    
    return n * factorial(n-1)

if __name__ =='__main__':
    num=int(input('Escribe un numero: '))
    r=factorial(num)
    m='el factorial es ',r
    print(m)
