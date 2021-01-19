n = int(input())
# h = n // 60**2
# n = n - h * 60**2

# m = n // 60
# n = n - m*60

# s = n
h = n//3600
m = (n-h*3600)//60
s = abs(n-((n-h*3600)+(n-m*60)))

print('{}:{}:{}'.format(h, m, s))
