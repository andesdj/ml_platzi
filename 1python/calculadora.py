def fex(a):
    mx_to_col=145.97
    return mx_to_col*a
def run():
    print ('Calculadora de divisas AMG')
    print('COnvierte Pesos MX a Pesos COL')
    amount=float(input('Ingresa la cantidad de pesos MX: '))
    r=fex(amount)
    
    print('${} Pesos Mexicanos son ${} Pesos Colombianos'. format(amount,r))
    print(' ')

if __name__ =='__main__':
    run()

