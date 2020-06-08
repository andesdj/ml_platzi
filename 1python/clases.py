# -*- coding: utf-8 -*-
class Lamp:
    _LAMPS= [
 '''
         |
 \     _____     /
     /       \
    (         )
-   ( ))))))) )   -
     \ \   / /
      \|___|/
  /    |___|    \
       |___| 
       |___| 
       
''' ,
     
''' 
  ..---..
 /       \
|         |
:         ;
 \  \~/  /
  `, Y ,'
   |_|_|
   |===|
   |===|
    \_/
''']
   
    def __init__(self,is_turned_on):
        self.is_turned_on=is_turned_on
    
    def turn_on(self):
        self.is_turned_on=True
        self._display_image()
    def turn_off(self):
        self.is_turned_on=False
        self._display_image()
    
    def _display_image(self):
        if self.is_turned_on:
           
            print(self._LAMPS[0])
           
        else:
            
            print(self._LAMPS[1])
          
            
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
            print("ADIOS")
            break

if __name__== '__main__':
    run()
    

                