print('--------------------------------------------------')
print("------- Seja muito bem vindo a FRUTARIA ES -------")
print('--------------------------------------------------')

nome = input('Por favor, digite o seu nome: ')
endereco = input('Digite o seu endereço: ')
ano = int(input('Digite o ano de nascimento: '))

venda = """
---------------------------------
|ID -- Fruta   ---  Preço(R$/kg)|
|A  -- Banana  ---  5.50        |
|B  -- Laranja ---  3.25        |
|C  -- Maçã    ---  7.80        |
|D  -- Uva     ---  5.40        |
|E  -- Kiwi    ---  17.20       |
---------------------------------
"""
print()
print('Temos disponíveis hoje as seguintes frutas')
print(venda)

op = input("Digite o ID da frta que você deseja comprar: ")
kg = float(input('Digite a qtde em kg que você deseja: '))

if op == 'A':
    fruta = 5.5
elif op == 'B':
    fruta = 3.25
elif op == 'C':
    fruta = 7.8
elif op == 'D':
    fruta = 5.4
elif op == 'E':
    fruta = 17.20
else:
    fruta = 0

valor = kg*fruta
frete = 5.0
if valor < 15:
    valor = valor + frete

idade = 2024 - ano
if idade > 60:
    valor = valor*0.95
    print('Olha, acabei de ver no sistema e você tem um desconto de 5% na compra!')

print()
print(nome, 'agradecemos a preferência.')
print('Sua compra será entregue em', endereco)
print('O valor total é de', valor)
