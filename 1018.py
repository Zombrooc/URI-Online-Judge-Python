num = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(num)

for nota in notas:
  qtndNotas = num//nota

  print("{} nota(s) de R$ {},00".format(qtndNotas, nota))

  num = num - (qtndNotas*nota)
