#escolha numero 0 a 5 e compare se é igual do computador
from json.encoder import ESCAPE_DCT
import random
pc = random.randint (0,5)
esc =int (input('Digite um numero entre 0 a 5: '))
print ('Numero do PC:    {}'.format(pc))
print ('Numero esolhido: {}'.format(esc))
if pc == esc:
    print ('Parabens!')
else:
    print ('Voce errou!')
    