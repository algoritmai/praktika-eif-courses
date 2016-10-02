__author__ = 'Marius'

temp = 0
A1 = 100
A2 = 120
DBD = 0
while A1 != A2:
    if A1 < A2:
        temp = A1
        A1 = A2
        A2 = temp
    A1 = A1 - A2
    DBD = A1
print('DBD yra:', A1)