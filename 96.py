d = []
for i in range(1, 20):
    d.append(input().split())

n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(1, 20):
        if d[j-1][int(y)-1] == 0:  # 가로값 고정, 세로값 변환
            d[j-1][int(y)-1] = 1
        else:
            d[j-1][int(y)-1] = 0

        if d[int(x)-1][j-1] == 0:  # 세로값 고정, 가로값 변환
            d[int(x)-1][j-1] = 1
        else:
            d[int(x)-1][j-1] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i-1][j-1], end=' ')
    print()
