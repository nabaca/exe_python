#escolha numero 0 a 5 e compare se é igual do computador
import random
from time import sleep
pc = random.randint (0,5)
esc =int (input('Digite um numero entre 0 a 5: '))
print ('Processando...')
sleep(2)
print ('==' *20)
print ('Numero do PC:    {}'.format(pc))
print ('Numero esolhido: {}'.format(esc))
print ('==' *20)
if pc == esc:
    print ('Parabens!')
else:
    print ('Voce errou!')
    