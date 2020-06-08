# -*- coding: utf-8 -*-
dicc= {}
dicc['primer elemento']='Hola'
dicc['segundo elemento']='Adios'

dicc['primer elemento']

#------------------EJEMPLO 2
calif={}

calif['algoritmos'] =9
calif['matematicas']=10
calif['web']=8
calif['db']=10

for key in calif:
    print(key)
    
for value in calif.values():
    print(value)
    
for key, value in calif.items():
    print('Llave: {}, Valor: {} '.format(key,value))
    
suma=0

for c in calif.values():
    suma+=c
    

cant=len(calif.values())
promedio =suma/cant
print("La suma es: ", suma)
print("La cantidad de asignaturas son: ",cant)
print("El promedio es: ",promedio)