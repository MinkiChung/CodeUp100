n, m = map(int, input().split())
d = []

for i in range(n):
    d.append([])

for i in range(n):
    for j in range((i+1)+(m-1)*n, i, -n):
        d[i].append(j)

for i in range(n-1, -1, -1):
    for j in range(m):
        print(d[i][j], end=' ')
    print()