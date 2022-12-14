def PW1(x, y):
    return x  + y + 3 >= 41  or x * 2 + y >= 41 or x + y * 2 >= 41

def PPG(x, y):  # гарантировано
    return not PW1(x, y) and PW1(x + 2, y + 1) and PW1(x * 2, y) \
           and PW1(x, y * 2) and PW1(x + 1, y + 2)


def PPM(x, y):  # возможно
    return not PW1(x, y) and (PW1(x + 2, y + 1) or PW1(x * 2, y)
                              or PW1(x, y * 2) or PW1(x + 1, y + 2))

def PW2(x,y):
    return PPG(x + 2, y + 1) or PPG(x * 2, y) \
           or PPG(x, y * 2) or PPG(x + 1, y + 2)

def PP(x,y):
    return (PW1(x + 2, y + 1) or PW2(x + 2, y + 1)) \
           and (PW1(x * 2, y) or PW2(x * 2, y)) \
           and (PW1(x, y * 2) or PW2(x, y * 2)) \
           and (PW1(x + 1, y + 2) or PW2(x + 1, y + 2))

ppm,ppg, pw2, pp = [], [], [], []

for i in range(1,41):
    if PPM(8, i):
        ppm.append(i)
    if PPG(8, i):
        ppg.append(i)
    if PW2(8, i):
        pw2.append(i)
    if PP(8, i):
        pp.append(i)
print("Возможный проигрыш за один ход:", *ppm)
print("Проигрыш за один ход:", *ppg)
print("Выигрыш за 2 хода:", *pw2 )
print("Проигрыш за 1-2 хода:", *pp)

