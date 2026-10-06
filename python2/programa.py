# 9 - Crie um programa com uma variável número qualquer. Depois, crie uma variável chute pedindo para o usuário digitar um número. Na sequência, crie uma condição para saber se o chute é igual a variável. Caso seja igual exiba uma mensagem "Você acertou", se for diferente exiba a mensagem "Você errou"

#numero = 1 
#c#hute = int(input('digite um numero'))
#if chute == numero:
   # print('você acretou')
#else:
    #print('você errou')

numero = 10
chute = int(input('Digite um numero'))
if chute == numero:
    print('você acertou')
elif chute > numero:
    print('você errou! o seu chute foi maior que o numero')   
elif chute > numero:
    print('você errou! o seu chute foi menor que o numero')   
numero = 10
while numero >= 10:
    print(numero)
    #numero = numero + 1
    numero += 1
numero_secreto = 50
total_tentativas = 5
while total_tentativas > 0:
    chute = int(input('digite seu numero'))
    print(f'Você digitou: {chute}')
    numero_certo = numero_secreto == chute
    numero_maior = chute > numero_secreto
    numero_menor = chute < numero_secreto
    if numero_certo:
        print('Você acertou!')
        break
    elif numero_maior:
        print('Você digitou um numero maior')
    else:
        print('Você digitou um numero menor')

    total_tentativas = total_tentativas - 1