# -*- coding: utf-8 -*-
def run():
    
    with open('a.txt', 'w', encoding="utf8") as ff:
        for line in ff:
            counter+=line.count('Beatriz')
    print ('Beatriz se encuentra {} veces en el texto'.format(counter))
    
if __name__ =='__main__':
    run()
