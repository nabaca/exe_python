import random
#from random import shuffle
n1 = input ('nome1 ')
n2 = input ('nome2 ')
n3 = input ('nome3 ')
n4 = input ('nome4 ')
lista = [n1, n2, n3, n4]
random.shuffle (lista)
#shuffle (lista)
print ('A ordem foi {}'.format (lista))