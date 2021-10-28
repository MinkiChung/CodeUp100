n = int(input())
d = []
for i in range(n):
    d.append([])

for i in range(n):
    for j in range(1+i*n, (i+1)*n+1):
        d[i].append(j)

for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print()