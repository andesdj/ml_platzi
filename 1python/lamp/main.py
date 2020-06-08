# -*- coding: utf-8 -*-
from lamp import Lamp

def run():
    lamp=Lamp(is_turned_on=False)
    while True:
        command=str(input('''Elige una opción:
            [P] Prender
            [A] Apagar
            [S] Salir
            '''))
            
        if (command=='p' or command=='P') :
            lamp.turn_on()
        
        elif(command=='a' or command=='A'):
            lamp.turn_off()
        else:
            print(" A D I O S ")
            break

if __name__== '__main__':
    run()
    