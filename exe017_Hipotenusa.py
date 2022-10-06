from math import (hypot)
co = float (input ('Cateto oposto '))
ca = float (input ('Cateto adjacente '))
#print ('A hipotenusa é {:.2f}'.format(hypot(ca,co)))

hi = hypot(co,ca)
print ('A hipotenusa é {:.2f}'.format (hi))