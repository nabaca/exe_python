#salario
s = float (input('Salário: '))
if s > 1250:
    print ('Aumento de 10 %: {:.2f}'.format((s*0.10)+s))
else:
    print ('Aumento de 15%: {:.2f}'.format((s*0.15)+s))


#salario + (salario * 15 / 100)