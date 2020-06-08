# -*- coding: utf-8 -*-
def averagetemp(tparam):
    sot=0
    for t in tparam:
        sot+=float(t)
    return sot/len(tparam)
        


if __name__ =='__main__':
    temp=[21,24,26,23,28,30,17]
    awg=averagetemp(temp)
    print('La temperatura Promedio es de: {}'.format(round(awg,3)))