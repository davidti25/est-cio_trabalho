## Ordem de precedência dos operadores em Python
# 1. Parênteses: ()
# 2. Exponenciação: **
# 3. Multiplicação, Divisão, Divisão Inteira, Módulo: *, /, //, %
# 4. Adição e Subtração: +, -
'''
n1 = int(input("Digite um número: "))
#05
print("O número escolhido foi: {} e o sucessor dele é: {} e o seu antecessot é: {}".format(n1, (n1+1),(n1-1)))
#06
print("Seu número é: {} / O dobro dele é: {}  / O triplo dele é: {} / A raiz quadrada dele é: {:.2f}".format(n1, (n1*2), (n1*3), (n1**(1/2))))
#07
nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite mais uma nota: '))

media = (nota1 + nota2) / 2

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, media))

#08

metro = float(input('Conversão de metros para centímetros e milímetros.\nDigite o valor em metros: '))

cent = metro * 100
mili = metro * 1000

print('O valor de {:.2f} metros corresponde a {:.2f} centímetros e {:.2f} milímetros.'.format(metro, cent, mili))


#09

print('==' * 20)
print('Calculadora')
print('==' * 20)

n1 = int(input('Qual tabuada você quer ver? '))

print('==' * 20)
print('Tabuada de {}'.format(n1))
print('==' * 20)
print('{} x {:2} = {}'.format(n1, 1, n1*1))
print('{} x {:2} = {}'.format(n1, 2, n1*2))
print('{} x {:2} = {}'.format(n1, 3, n1*3))
print('{} x {:2} = {}'.format(n1, 4, n1*4))
print('{} x {:2} = {}'.format(n1, 5, n1*5))
print('{} x {:2} = {}'.format(n1, 6, n1*6))
print('{} x {:2} = {}'.format(n1, 7, n1*7))
print('{} x {:2} = {}'.format(n1, 8, n1*8))
print('{} x {:2} = {}'.format(n1, 9, n1*9))
print('{} x {:2} = {}'.format(n1, 10, n1*10))
print('==' * 20)


#10

print('==' * 20)
print('Conversor de Moedas')
print('==' * 20)

real = float(input('Digite o valor em R$ que você deseja converter: R$ '))

dolar = real / 5.25
euro = real / 5.10

print('Com R$ {:.2f} você pode comprar US$ {:.2f} dólares ou € {:.2f} euros.'.format(real, dolar, euro))


#11

print('==' * 20)
print('Calculo de Pintura')
print('==' * 20)

parede_altura = float(input('Digite a altura da parede em metros: '))
parede_largura = float(input('Digite a largura da parede em metros: '))

area_parede = parede_altura * parede_largura
tinta_necessaria = area_parede / 2

print('A área da parede é de {:.2f} metros quadrados.'.format(area_parede))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(tinta_necessaria))


#12

print('==' * 20)
print('Calculadora de Desconto')
print('==' * 20)

preco_produto =  float(input('Digite o preço do produto: R$ '))

desconto = preco_produto * 0.05
preco_final = preco_produto - desconto

print('O preço do produto com 5% de desconto é: R$ {:.2f}'.format(preco_final))
print('Seu desconto foi de: R$ {:.2f}'.format(desconto))

'''
#13

print('==' * 20)
print('Calculadora de Aumento Salarial')
print('==' * 20)

salario_atual = float(input('Digite o salário atual do funcionário: R$ '))
aumento = salario_atual * 0.15
salario_novo = salario_atual + aumento

print('Seu atual salário é: R$ {:.2f}'.format(salario_atual))
print('Com o aumento de 15%, seu novo salário será: R$ {:.2f}'.format(salario_novo))
print('O valor do aumento foi de: R$ {:.2f}'.format(aumento))

