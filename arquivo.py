#  1- Crie um variável mensagem e exiba uma mensagem na tela 
# 2- Crie um variável número e exiba esse número na tela
# 3- Crie duas variáveis numéricas e faça as 4 operações matemáticas com esses números. Faça também a exponenciação e o resto da divisão
# 4- Crie duas variáveis de texto e faça a concatenação dessas mensagens
# 5- Faça um programa que receba um texto e faça-o repetir 5 vezes
#  6- Crie uma variável de texto em minúsculo e deixe-o com todas as letras maiúsculas
# 7- Crie um programa que recebe um texto do usúario e exiba na tela 
# 8- Crie um programa que receba do usuário nome, idade, altura, cidade e estado e exiba a seguinte frase na tela: "Olá" meu nome é ____________, tenho_______ anos de idade. moro na cidade de _________/________".Use printf
# 9- Crie um programa com uma variável número qualquer. Depois, crie uma variável chute pedindo para o  usuário digitar um número. Na sequência, crie uma condição para saber se o chute é igual a variável. Caso seja igual exiba uma mensagem "Você acertou", se for diferente exiba a mensagem "Você errou"

mensagem = 'meu nome é Pedro'
print(mensagem)

numero = 6 
print(numero)

numero2 = 7
soma = numero + numero2
print(soma)

numero3 = 10
numero4 = 20
soma = numero3 + numero4
div = numero3 / numero4
sub = numero3 - numero4
multi = numero3 * numero4
print(soma)
print(div)
print(sub)
print(multi)

expo = numero3**numero4
Resto___dive = numero4 % numero3
Divi_Inteira = numero // numero2
print(expo)
print(Resto___dive)
print(Divi_Inteira)

texto1 = "batata"
texto2 = "banana"
c = texto1 + " " + texto2
print(c)

text = "aula"
repeticao = text * 5
print (repeticao)

text2 = 'bom dia'
#text2.upper()
print(text2.upper())

texto = input("Coloque sua mensagem")
print(texto)

nome2 = input (" digite seu nome") 
idade = int (input("digite sua idade"))
altura = float (input("digite sua altura"))
cidade = input(" digite sua cidade")
estado = input ("digite seu estado")

print (f'meu nome é {nome2}, tenho {idade} anos de idade. Moro na cidade de {cidade} do estado de {estado}. minha altura é {altura}') 