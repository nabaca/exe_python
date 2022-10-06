'''import math
ang = float (input('Angulo '))
sen = math.sin(math.radians (ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('O Ângulo de {} tem \nCosseno {:.2f} \nSeno {:.2f} \nTangente {:.2f}'.format(ang, cos, sen, tan))'''

from math import sin, cos, tan, radians
ang = float (input('Digite o angulo '))
s = sin (radians (ang))
c = cos (radians(ang))
t = tan (radians(ang))
print ('O Seno é {:.2f} \n O Cosseno é {:.2f} \n A Tangente é {:.2f}'.format (s,c,t))