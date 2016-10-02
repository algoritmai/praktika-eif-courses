__author__ = 'Marius'

# Didžiausio bendrojo daliklio algoritmas

def DBD(A, B): # A ir B, DBD skaičiavimui
    print('Pradinės reikšmės: ', 'A =', A, ' B =', B)
    i = 1
    while B != 0: # Kol B nelygus nuliui ieškom
        temp = B  # B patalpinama į laikinajį kintamajį
        print (i,'ciklo iteracija. Į laikiną temp kintamąjį patalpinama B =',temp,', tada', A,' mod ', B, '=', A % B)
        B = A % B # A mod B, jei = nulis tai yra DBD
        A = temp # A priskiriame laikinąjį kintamajį
        i += 1
    return A # Gražinamas DBD kadangi buvo išsaugotas temp
print('Didžiausias bendras daliklis (DBD) yra:',DBD(950, 100))




