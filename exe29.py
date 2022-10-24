#ultrapassar 80 km , mensagem multado e R$ 7,00 por km ultrapassado
v = int(input('Digite a Velocidade: '))
print ('Sua velocidade: {} Km'.format (v))

if v <= 80:
    print ('Sem multas!')
else:
    r = (v - 80)
    r1 = r * 7
    print ('Ultrapassou {} km'.format(r))
    print ('Multado R$ 7,00 por Km. Total R$ {:.2f}'.format(r1))
