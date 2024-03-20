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
def calcular_valor(valor_compra):
    if 0.01 <=  valor_compra < 10.00 :
        desconto = 0
    elif 10.00 <= valor_compra < 100.00:
        desconto = 0.05
    elif 100.00 <= valor_compra < 500.00:
        desconto = 0.10
    else:
            desconto = 0.15

    valor_final=  valor_compra * ( 1 - desconto)
    return valor_final , desconto * 100

#Ex04
def validar_codigo(codigo):
     if len(codigo) != 7:
        return False
     if not codigo.startswitch("BR"):
          return False
     if not codigo[2:6].isdigit():
          return False
     if not(1<=int(codigo[2:6])<=9999):
          return False
     if codigo[-1] != "X":
          return False
     return True

#Ex05
def verificar_codigo():
     codigo = input("Digite o código do funcionário: ")
     if  validar_codigo(codigo):
          print("Código valido.")
     else:
          print("Código inválido.")
     

#Ex06
def calcular_aquario(comprimento, altura, largura, temperatura_desejada, temperatura_ambiente):
    volume = (comprimento * altura * largura) / 1000
    potencia_termostato = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    filtragem_por_hora = 2 * volume 
    return volume, potencia_termostato, filtragem_por_hora

#Ex07
def calcular_imc():
     peso = float(input("Digite seu peso em kg: "))
     altura = float(input("Digite sua altura em metros: "))
     imc = peso / (altura * altura)

     if   imc < 18.5:
       print("Baixo peso")
     elif  18.5 <= imc <= 24.9:
        print("Peso normal")
     elif  25.0 < imc <= 29.9:
        print("Acima de peso")
     elif  30.0 <= imc <= 34.9:
        print("Obesidade I")
     elif  imc > 34.9 :
        print("Obesidade II/III")

