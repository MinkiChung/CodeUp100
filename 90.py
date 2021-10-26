a, m, d, n = map(int, input().split())
if n == 1:
    print(a)
else:
    for i in range(1, n):
        a = (a * m) + d
        if i == n - 1:
            print(a)
