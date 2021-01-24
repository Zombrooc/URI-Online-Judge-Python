num = float(input())

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
  qtndNotas = num//nota

  print("{} nota(s) de R$ {}".format(int(qtndNotas), nota))

  num = num - (qtndNotas*nota)
print('MOEDAS:')
for moeda in moedas:
  qtndMoedas = num//moeda

  print("{} moeda(s) de R$ {:.2f}".format(int(qtndMoedas), moeda))

  num = num - (qtndMoedas*moeda)