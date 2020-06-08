# -*- coding: utf-8 -*-
import random
def run():
    nf=False
    rand=random.randint(1,20)
    print("Secret N ",rand)
    
    while not nf:
        n=int(input('Ingrese un número entre 1 y 20: '))
        if n==rand:
            print ('Correcto! el nunero es ',n)
            nf=True
        elif n>rand:
            print("El numero es mas pequeño que ", n)
        else: 
            print("El Número es mas grande que ", n)
            

if __name__ =='__main__':
    run()