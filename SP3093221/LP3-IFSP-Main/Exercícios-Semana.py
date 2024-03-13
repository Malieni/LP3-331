#Ex01

num = int(input('Digite um número: '))
sucessor = num  + 1
antecessor = num - 1
print (f'O numero {num} tem como sucessor {sucessor} e o antecessor é {antecessor}')

#Ex02

n1 = float(input('Primeiro valor:'))
n2 = float(input('Segundo valor:'))
n3 = float(input('Terceiro valor:'))

media = (n1 + n2 + n3)/3

print('A média dos números é  {:.2f}' .format(media))

#Ex03

valor = int(input('Digite o valor do produto  : R$'))
if valor >= 0.01 and valor <= 9.99:
    print('o seu produto não tem desconto')

if valor >=10.00 and  valor <= 99.99 :
    desconto = valor * 0.05

if  valor >= 100.00 and valor <=499.99 :
    desconto = valor *  0.10
    
if valor >= 500.00  :
    desconto = valor * 0.15

print(f'O desconto do seu produto é {valor}')



