'''n = str (input('Numero de 0 a 9999: '))
print ('O número ', n)
print ('Unidade ', n[3])
print ('Dezena  ', n[2])
print ('Centena ', n[1])
print ('Milha   ', n[0])'''




n = int (input('Numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print ('u {}'.format(u))
print ('d {}'.format(d))
print ('C {}'.format(c))
print ('m {}'.format(m))