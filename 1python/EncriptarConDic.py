# -*- coding: utf-8 -*-
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}
def cypher(m):
    words=m.split(' ')
    c_msg=[]
    
    for word in words:
        c_word=''
        for letter in word:
            c_word +=KEYS[letter]
        c_msg.append(c_word)
        
    return ' '.join(c_msg)

def dcypher(m):
    words=m.split(' ')
    d_msg=[]
    
    for word in words:
        d_word=''
        for letter in word:
            for key , value in KEYS.items():
                if value==letter:
                    d_word+=key
        d_msg.append(d_word)
        
        return ' '.join(d_msg)
    
    

def run():
    while True:
        command= str(input('''
Bienvenido a  criptografía AMG. ¿Que deseas hacer?
                           
   [C] CIFRAR Mensaje
   [D] DECIFRAR Mensaje
   [S] SALIR
                           
        '''))
    
        if (command =='C') or (command=='c'):
            print("Cifrar")
            print('-------------------------------')
            msg=str(input('Escribe tu mensaje: '))
            
            print('El mensaje cifrado es:')
            cypher_msg=cypher(msg)
            print(cypher_msg)
       
        elif (command =='D') or (command=='d'):
            print("Desifrar")
            print('-------------------------------')
            msg=str(input('Escribe tu mensaje cifrado: '))
            dcypher_msg=dcypher(msg)
            print('El mensaje descifrado es:')
            print(dcypher_msg)
            
        else:
            print("SALIR")

if __name__ =='__main__':
    run()
