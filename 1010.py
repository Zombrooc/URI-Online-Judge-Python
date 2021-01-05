# -*- coding: utf-8 -*-
A = str(input())
B = str(input())

infoA = A.split(' ')
infoB = B.split(' ')

answer = (int(infoA[1]) * float(infoA[2])) + (int(infoB[1]) * float(infoB[2]))

print('VALOR A PAGAR: R$ {:.2f}'.format(answer))