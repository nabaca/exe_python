frase = 'Curso em vídeo Python'
print ('*******************************************')
print (frase[::5])
print (frase.count('e', 0, 13))
print (frase.upper())
print (frase.lower())
print (frase.upper().count('O'))
print (frase.capitalize())
print (frase.title())
print (len(frase))
print (len(frase.lstrip())) #remove desnecessarios l esq, r dir, strip dois lados#
print (frase.replace('em', 'DO'))
frase = frase.replace('vídeo', 'M')
print (frase)
frase = 'Curso em video python'
print (frase)
print ('Curso' in frase)
print (frase.find ('curso1'))
print (frase.find ('Curso')) #mostra a posição que inicia a palavra#
print (frase.lower().find ('curso'))
print (frase.split())
print('*'.join(frase))
div = frase.split()
print('*'.join(div))
print (div)
print(''.join(div))
print (div[3][4])



frase = "Mundo mundo vasto mundo"
print(frase[::-1])