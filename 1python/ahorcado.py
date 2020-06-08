# -*- coding: utf-8 -*-
import random
IMAGES = [ '''
          +---+
          |   |
              |
              |
              |
              |
              |
              |
              ==============''', '''
              
          +---+
          |   |
          O   |
              |
              |
              |
              |
              |
              ==============''', '''
              
          +---+
          |   |
          O   |
          |   |
              |
              |
              |
              |
              ==============''', '''             
 
          +---+
          |   |
          O   |
         /|   |
              |
              |
              |
              |
              ==============''', '''  
              
          +---+
          |   |
          O   |
         /|\  |
              |
              |
              |
              |
              ==============''', '''               
        
          +---+
          |   |
          O   |
         /|\  |
          |   |
              |
              |
              |
              ==============''', '''         
              
          +---+
          |   |
          O   |
         /|\  |
          |   |
         /    |
              |
              |
              ==============''', '''   

              
          +---+
          |   |
          O   |
         /|\  |
          |   |
         / \  |
              |
              |
              ==============''', '''   '''
       
]
WORDS=['lavadora','secadora' , 'sofa', 'ministerio', 'arquitecto', 'teclado']

#Generar un numero aleatorio desde el tamaño de la lsita WORDS y elige una palabra
def random_word():
    idx= random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def displayboard(hw,t):
    print(IMAGES[t])
    print('')
    print(hw)
    print('_______________________________________')    

# Elegimos palabra al azar con Random Word
# A partir del tamaño de la palabra, rellena hidden word con _ multiplicando
# Pone intentos en 0 y ejecuta el bucle while
# Con displayboard define el tablero de juego

def run():
    word=random_word()
    hidden_word=['_']*len(word)
    tries=0
    
    while True:
        displayboard(hidden_word,tries)
        current_letter= str(input('Escoge una letra: '))
        letter_indexes =[]
        
        for idx in  range(len(word)):
            if word[idx]==current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes)==0:
            tries+=1
            
            if tries>=7:
                displayboard(hidden_word, tries)
                print('')
                print('Perdiste!! La palabra correcta era {}'.format(word))
                break
            
        else:
            for idx in letter_indexes:
                hidden_word[idx]=current_letter
            
            letter_indexes=[]
# Detectar el error, en python aparece el error y para el programa
        try:            
            hidden_word.index('_')
        except ValueError:
            print('')
            print('FELICIDADES! Ganaste. La palabra es {}'.format(word))
            break
        

# Inicio del juego
if __name__ == '__main__':
    print('B I E N V E N I D O S   -  A H O R C A D O S')
    run()