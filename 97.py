h, w = map(int, input().split())
n = int(input())
ls = []
for i in range(n):
    ls.append([])
    ls[i].extend(map(int, input().split()))

arr = []
for i in range(h):
    arr.append([])
    for j in range(w):
        arr[i].append(0)

# 막대 놓기
# 0가 1세
for i in range(n):
    # ls[i][0], ls[i][1], ls[i][2], ls[i][3]
    if ls[i][1] == 0:
        for j in range(ls[i][3] - 1, ls[i][3] + ls[i][0] -1):
            arr[ls[i][2] - 1][j] = 1
    else:
        for j in range(ls[i][2] - 1, ls[i][2] + ls[i][0] -1):
            arr[j][ls[i][3] - 1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()