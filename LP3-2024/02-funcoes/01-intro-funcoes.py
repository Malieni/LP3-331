# Funcao 
#modularizar o programa 
# reuso 
# manuntenabilidade 

#só pode acessar hora estiver entre 8h e 18h 
hora_atual = 12 

if hora_atual >= 8 and hora_atual <=18:
        print('permitido o acesso')

#entrada = hora atual 
#saida se está dentro ou não do horario comercial 

def dentro_horario_comercial(hora_atual):
        if  hora_atual >= 8 and hora_atual <= 18: 
                return True 
        else: 
             return False 
        
def dentro_horario_comercial(hora_atual):
       return hora_atual >= 8 and hora_atual<= 18


#Declaracao 
#def nome_funcao():
#   Corpo da funcao 
#   Corpo da funcao 

#funcao com retorno 
def diga_ola(nome):
       print(f"Ola (nome)")

#Chamada 
diga_ola('Marcos')

#funcao com retorno 
def montar_frase(nome):
       return f'Olá, eu sou o {nome}'

nome = 'Marcos'
print(montar_frase(nome))



#Parametro e argumentos 
#Parametros sao referencias podem ser acessadas 
# dentro da funcao 
# e o argumento sao os valores passados para os parametros

def somar(numero1 , numero2): 
       return numero1 + numero2 

somar ( 10.0 , 5.0)
#Podemos atribuir u valor direto no parametro ou na chamada da funcao


#escopo de variaveis 
# variavel local

def calcular_media(nota1 , nota2 , nota3):
       media = (nota1 + nota2 + nota3 )/ 3
       return media

#print (media)

#variavel global 
total = 0.0 

def soma (n1 , n2 , n3):
       #global total
       total  = total + n1 + n2 + n3
       return total

print(total)
soma(4.0 ,6.0 ,8.0)
print(total)


#Parametros com valor padrão (default)
def gerar_boas_vindas(mensagens,nome):
       return  f'{mensagens}, {nome}'

print(gerar_boas_vindas('Bom dia','Marcos'))
print(gerar_boas_vindas('Boa tarde', 'Joao'))
print(gerar_boas_vindas(nome = 'Maria'))
print(gerar_boas_vindas('Maria'))

def gerar_boas_vindas(nome, mensagens='Bom dia'):
       return  f'{mensagens}, {nome}'

print(gerar_boas_vindas('Bom dia','Marcos'))
print(gerar_boas_vindas('Boa tarde', 'Joao'))
print(gerar_boas_vindas(nome = 'Maria'))
print(gerar_boas_vindas('Maria'))


#Argumentos nomeados
print(gerar_boas_vindas(nome = 'Maria'))


#Docstring
#comentario da documentacao 
def somar(n1,n2):
       '''
       Funcao que soma dois numeros 
       
       param n1: primeiro numero
       param n2: segundo numero 
       return : soma
       '''

