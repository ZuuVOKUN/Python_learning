import random

sn = random.randint(1, 100)
pn = 1
ns = 1
tn = 100
n = sn
p = pn




while n < tn:
    p += 1
    n += ns
    print(n)

    while True:
        n = n + ns
        print(n)
        if n >= tn:
            print('НАКОНЕЦТО!!!')
            break