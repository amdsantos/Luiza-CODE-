print('-------- EXERCÍCIO 18 --------')
nota = int(input("Informe o valor da sua nota: "))
if nota < 0 or nota > 100:
  print('Nota invalida')
elif nota > 60:
  print('Parabéns! Você foi aprovado.')
else:
  print('Você não foi aprovado.')