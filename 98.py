d = []
for i in range(10):
    d.append(input().split())

n = 1
m = 1
while d[m][n] == '0':
    d[m][n] = '9'
    if d[m][n + 1] == '0':
        n += 1
    elif d[m][n + 1] == '1':
        m += 1
    elif d[m][n + 1] == '2':
        d[m][n + 1] = '9'
        break

if d[m][n] == '2':
    d[m][n] = '9'

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()