n = int(input())
i = 1
sum = 0
while True:
    if sum < n:
        sum += i
        i += 1
    else:
        print(i-1)
        break