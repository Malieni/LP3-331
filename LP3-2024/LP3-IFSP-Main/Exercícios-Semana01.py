#Ex01
numero_usuario = int 
adivinhar = 5 
print(' Tente adivinhar o numero estabelecido entre 0 a 100')
while numero_usuario!= adivinhar:
    numero_usuario = int (input('Entre com um numero:  '))
    if numero_usuario == adivinhar:
        print('você acertou o numero')
    if numero_usuario> 5 and numero_usuario<= 10:
        print('Quase!')
    elif numero_usuario<5 and numero_usuario>= 0:
        print('Está perto')
    elif numero_usuario> 10:
        print('Está longe')


#Ex02 
def tabela_multiplicacao(numero):

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
numero = int(input('Entre com numero para criar tabela de multiplicação: '))
tabela_multiplicacao(numero)



#Ex03
import re
def conta_letras(texto):
    vogais = 0
    consoantes = 0

    texto = re.sub('[^a-zA-Z]', '', texto)

    for letra in texto:
        if letra.lower() in 'aeiou':
            vogais += 1
        else:
            consoantes += 1

    return {'vogais': vogais, 'consoantes': consoantes}

frase = input('Digite uma frase: ')
resultado = conta_letras(frase)
print(f'Número de vogais: {resultado["vogais"]}')
print(f'Número de consoantes: {resultado["consoantes"]}')

#Ex04

candidatos = {"1": 0, "2": 0, "3": 0}
while True:
    voto = input(" Digite o número do candidato que deseja votar (1-Motta, 2-Luk, 3-Latorre, 0-Sair): ")
    if voto == "0":
        break
    elif voto in candidatos:
        candidatos[voto] += 1
    else:
        print("Opção inválida. Tente novamente.")

for candidato, votos in candidatos.items():
    print(f"Candidato {candidato}: {votos} votos")

voto_max = max(candidatos.values())
for candidato, votos in candidatos.items():
    if votos == voto_max:
        print(f"O vencedor é o Candidato {candidato} com {votos} votos!")


#Ex05 
def palindromo(palavra):

    palavra = palavra.lower()
    palavra_digitada = ''.join(c for c in palavra if c.isalnum())
    return palavra_digitada == palavra_digitada[::-1]

if __name__ == "__main__":
    palavra = input(" Coloque a palavra ou frase para checkar se é palindromo: ")
    resultado = palindromo(palavra)
    print(f"O '{palavra}' é palindromo? {'Sim' if resultado else 'Não'}")


#Ex06
def converter_notas(notas):
    if 90 <= notas <= 100:
        return "A"
    elif 80 <= notas < 90:
        return "B"
    elif 70 <= notas < 80:
        return "C"
    elif 60 <= notas < 70:
        return "D"
    else:
        return "F"

# Example usage
nota_usuario = int(input("Entre com as notas de (0-100): "))
grade_nota = converter_notas(nota_usuario)
print(f"A letra da sua nota é: {grade_nota}")


#Ex07
import random

def jogo_forca():
    palavras = ['python', 'programa', 'luk', 'latorre', 'variavel']
    palavra_pra_acertar = random.choice(palavras)
    letras_digitadas = []
    tentativas = 7
    palavra_encontrada = ['_'] * len(palavra_pra_acertar)

    while tentativas > 0 and '_' in palavra_encontrada:
        print("\nTentativas restantes: ", tentativas)
        print("Palavra encontrada: ", ' '.join(palavra_encontrada))
        letra_usuario = input("digite uma letra: ").lower()

        if letra_usuario in letras_digitadas:
            print("Você ja usou está letra ! Tente outra.")
        else:
            letras_digitadas.append(letra_usuario)

            if letra_usuario in palavra_pra_acertar:
                for index, letra in enumerate(palavra_pra_acertar):
                    if letra == letra_usuario:
                        palavra_encontrada[index] = letra
            else:
                tentativas -= 1

    if '_' in palavra_encontrada:
        print("Acabou o número de tentativas... ;-; A palavra era", palavra_pra_acertar)
    else:
        print("Parabéns você acertou a palavra:", palavra_pra_acertar)

jogo_forca()








#Ex08
import re

def conta_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    contador = {}

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    return contador

texto1 = input("Digite o texto: ")
resultado1 = conta_palavras(texto1)
print(resultado1)

texto2 = input("Digite outro texto: ")
resultado2 = conta_palavras(texto2)
print(resultado2)