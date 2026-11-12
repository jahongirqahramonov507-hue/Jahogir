n=5
a=[[0]*n for _ in range(n)]
from random import randint
for i in range(n):
    for j in range(n):
        a[i][j]=randint(1,50)
print("avval")
for qator in a:
    print(qator)
print("keyin")
for i in range(n//2):
    for j in range(i, n-1-i):
        a[i][j], a[n-1-j][i], a[n-1-i][n-1-j], a[j][n-1-i] = \
        a[j][n-1-i], a[i][j], a[n-1-j][i], a[n-1-i][n-1-j]
for qator in a:
    for element in qator:
        print(element, end=" ")
    print()
