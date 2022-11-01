#viagem - 0.50 até 200km / 0.45 mais que 200
d = int (input('Distancia da viagem '))
if d <=200:
    print ('Viagem abaixo de 200 km (0.50 o km)')
    print ('Valor {:.2f}'.format(d*0.50))
else:
    print ('Viagem acima de 200 km (0.45 o km)')
    print ('Valor {:.2f}'.format (d*0.45))
print ('FIM')
#------------------------------------------------
if d<=200:
    p = d*0.50
else:
    p = d*0.45
print ('O valor é {:.2f}'.format(p))
#------------------------------------------------
p = d*0.50 if d<=200 else d*0.45
print ('O valor é {:.2f}'.format(p))