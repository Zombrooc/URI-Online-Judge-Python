# -*- coding: utf-8 -*-
name = str(input())
salary = float(input())
selling = float(input())

answer = salary + (selling*0.15)

print('TOTAL = R$ {:.2f}'.format(answer))