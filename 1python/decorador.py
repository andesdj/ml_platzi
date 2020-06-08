# -*- coding: utf-8 -*-

def protected(func):
    
    def wrapper(password):
        if password=='andes':
            return func()
        else:
            print ("Contraseña no válida :(")
    return wrapper

@protected    
def protected_f():
    print('Tu contraseña es correcta!')
    

if __name__=='__main__':
    password=str(input("Escribe tu contraseña:"))
    protected_f(password)
    