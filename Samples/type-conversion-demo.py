'''
Daire alanı : r2
Daire çevresi : 2r2

* yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. r:3.14)

'''

pi = 3.14

r = input('yari cap:')
r = float(r)
alan = pi * (r**2)
cevre = 2 * pi * r
print('alan', alan)
print('cevre', cevre)

print('alan: ' + str(alan) + ' cevre: ' + str(cevre))