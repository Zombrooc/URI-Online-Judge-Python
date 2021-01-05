# -*- coding: utf-8 -*-

nums = str(input()).split(' ')

A = int(nums[0])
B = int(nums[1])
C = int(nums[2])

maxAB = (A+B+abs(A-B))/2

max = maxAB if maxAB>C else C

print("{:.0f} eh o maior".format(max))
