from operator import indexOf


d = int (input('Quantos dias '))
km = int (input('Quantos kms '))
total = (d*60)+(km*0.15)
#print ('O valor a pagar é ', ((d*60)+(km*0.15) ))
print ('O valor a pagar é {:.2f}'.format(total))
