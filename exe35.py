# 3 retas formam um triangulo~
a = float (input('Valor 1: '))
b = float (input('Valor 2: '))
c = float (input('Valor 3: '))
#print ('Sim, formam um triangulo' if a + b < c and a + c < b and b + c < c else ('Não formam um triangulo'))
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print ('\033[1;30;46mSim\033[m, formam um triangulo') 
else: 
    print ('\033[7;30;46mNão\033[m formam um triangulo')


if a < b + c and b < a +c and c < a + b:
    print ('Formam triangulo')
else:
    print ('Não formam triangulo')