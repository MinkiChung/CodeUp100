w, h, b = map(int, input().split(' '))
c = w * h * b /8/1024/1024
print(format(c, ".2f"), 'MB', sep=' ')