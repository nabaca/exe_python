'''nome = str(input('Seu nome ')).upper()
if nome == 'JOAO':
    print ('Olá seu nome é JOAO')
else:
     print('Seu nome não é João. Seu nome é ', nome)
print ('Bom dia {}'.format(nome))'''

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
print ('A média é: {:.2f}'.format (m))
print ('Parabéns!!' if m >=5.01 else 'Reprovado!!')
if m <= 5:
    print ('Reprovado!')
else:
    print ('Aprovado! Parabéns \n')
print ('FIM')