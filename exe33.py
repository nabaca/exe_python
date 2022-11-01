#maior e menor de tres numeros
from re import A


n1 = int (input('Digite 1 numero: '))
n2 = int (input('Digite 2 numero: '))
n3 = int (input('Digite 3 numero: '))
#mi = min (n1,n2,n3)
#ma = max (n1,n2,n3)
#print ('O menor é {}'.format(mi))
#print ('O maior é ',ma)

if n1<=n2 and n1<=n3:
   me = n1
if n2<=n1 and n2<=n3:
   me = n2
if n3<=n1 and n3<=n2:
    me = n3

if n1>=n2 and n1>=n3:
    ma = n1
if n2>=n1 and n2>=n3:
    ma = n2
if n3>=n1 and n3>=n2:
    ma = n3    
print ('O menor é: ',me)
print ('O maior é: ',ma)


#eliminando if
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3

ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3

print ('Menor: {}'.format(me))
print ('Maior: {}'.format(ma))