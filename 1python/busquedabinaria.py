# -*- coding: utf-8 -*-
def binsearch(n,ntf,l,h):
  
    if l>h:
        return False
    mm=int((l+h)/2)
    
    if n[mm]==ntf:
        return True
    elif n[mm]>ntf:
        return binsearch(n,ntf,l,mm-1)
    else:
        return binsearch(n,ntf,mm+1,h)


    return ntf
if __name__ =='__main__':
    numbers=[1,3,4,5,6,7,10,11,25,37,28,34,36,49,51]
    
    ntf=int(input("Ingrese un número: "))
    
    res= binsearch(numbers,ntf,0,(len(numbers))-1)
    if res is True:
        msg='El número está en la lista'
    else:
        msg='El número no está en la lista'
    print(msg)
    