'''
    faça um programa q leia 3 numeros e mostre o maior
'''

a = int(input('Primeiro: '))
b = int(input('segundo: '))
c = int(input('Terceiro: '))


if a >= b and a >=c :
       print (' Primeiro: %d' %a)
elif b>= c :
       print ('Segundo: %d' %b)
else:
       print ('Terceiro: %d' %c)
