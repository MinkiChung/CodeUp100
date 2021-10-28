n = int(input())
d = []
for i in range(n):
    d.append([])

for i in range(n):
    for j in range(i+1, i+n*(n-1)+2, n):
        d[i].append(j)

for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print()