# -*- coding: utf-8 -*-

nums = str(input()).split(' ')

pi = 3.14159

A = float(nums[0])
B = float(nums[1])
C = float(nums[2])

print("TRIANGULO: {:.3f}".format(A*C/2))
print("CIRCULO: {:.3f}".format(pi*C**2))
print("TRAPEZIO: {:.3f}".format(float((A+B)*C)/2))
print('QUADRADO: {:.3f}'.format(B**2))
print("RETANGULO: {:.3f}".format(A*B))
