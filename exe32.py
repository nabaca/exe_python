#anobissexto
from datetime import date
a = int (input('Digite o ano ou digite 0 para ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print ('SIM - Ano Bissexto')
else:
    print ('NÃO - Ano Bissexto')
print ('=====================')
#print ('Sim Bissexto' if a % 4 == 0 else ('Não Bissexto'))