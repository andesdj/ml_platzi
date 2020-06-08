# -*- coding: utf-8 -*-
pares=[]

for num in range(1,31):
    if num%2 ==0:
        pares.append(num)

even=[num for num in range(1,31) if num %2==0]


cuadrados={}

for num in range(1,11):
    cuadrados[num]=num**2

squares={num: num**2 for num in range (1,11)}