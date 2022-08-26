from functools import reduce

print( "------------ SAÍDA FUNÇÃO ------------")

def foo(value):
    print(f'Olá, esse é o parâmetro: {value}')
    
foo('Luiza Code')

lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 - 0.1)
  
print("\n------------ MAP ------------")
resultado = map(desconto, lista)
print(list(resultado))

print("\n------------ FILTER ------------")
valores = filter(lambda x: x > 100, lista)
print(list(valores))

print("\n------------ REDUCE ------------")
soma = reduce(lambda x, y: x+y, lista, 0)
print(soma)