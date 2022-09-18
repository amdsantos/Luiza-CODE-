print('-------- EXERCÍCIO 19 --------')

venda = float(input("Informe o valor da sua venda: "))
if venda > 1000 or venda > 5000:
  dez = (venda * 10) / 100
  print(f'Sua comissão em reais é R${dez}')
elif venda > 5000 or venda > 10000:
  vinte = (venda * 20) / 100
  print(f'Sua comissão em reais é R${vinte}')
elif venda > 10000 or venda > 50000:
  vintcinco = (venda * 25) / 100
  print(f'Sua comissão em reais é R${vintcinco}')
elif venda > 50000:
  trinta = (venda * 30) / 100
  print(f'Sua comissão em reais é R${trinta}')
else:
  print('Você não tem comissão')