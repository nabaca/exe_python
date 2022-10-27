# 3 retas formam um triangulo~
a = int (input('Valor 1: '))
b = int (input('Valor 2: '))
c = int (input('Valor 3: '))
#print ('Sim, formam um triangulo' if a + b < c and a + c < b and b + c < c else ('Não formam um triangulo'))
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print ('Sim, formam um triangulo') 
else: 
    print ('Não formam um triangulo')


