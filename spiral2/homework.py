def spiralize(size, n=1):
    x = n # starting number
    y = 2 #turn
    z = n #current number in progress
    r = 0 #used as a reset

    while z < pow(size, 2) + n - 1:
        z += y
        x += z
        r += 1
        if r == 4:
            y += 2
            r = 0
    return x

print(spiralize(501,15))
