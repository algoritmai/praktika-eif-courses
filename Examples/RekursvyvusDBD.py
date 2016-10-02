__author__ = 'Marius'
t = 0
def DBD(a, b):
    print('a =', a, ', b =', b)
    t = b
    b = a % b
    print('b =', b, ', t =', t)
    if b == 0:
        print('DBD yra:', t)
        return t
    else:
        return DBD(t, b)
DBD(522, 14)