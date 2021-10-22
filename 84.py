h, b, c, s = map(int, input().split(' '))
c = h * b * c * s / 8 / 1024 / 1024
print(format(c, ".1f"),'MB',sep=' ')