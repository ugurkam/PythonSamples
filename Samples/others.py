# Identity operator : is

# from traceback import print_tb


# x = y = [1, 2, 3]

# z = [1, 2, 3]


# print( x==y) # Değer karşılaştırması
# print( x==z) # Değer karşılaştırması


# print( x is y) # Referans tipindeki bir verinin adres karşılaştırması. True döner çünkü x ve y aynı adrese sahiptir.

# print( x is z) # Referans tipindeki bir verinin adres karşılaştırması. False döner çünkü x ve z aynı adres sahip değildir.




# from traceback import print_tb


# x = [1, 2, 3]
# y = [2, 4]

# del x[2]
# y[1] = 1
# y.reverse()

# print (x==y)
# print ( x is y) # Aynı objenin aynı adresi gösterip göstermediğini soruyoruz.

# print ( x is not y)  # x y objesi değil midir diye de sorabiliriz.


# Membership operator : in


x = ['banana', 'apple']
print('banana' in x)

name = 'burcak'

print('a' in name) # a name içinde var mı diye soruyoruz.
print('a' not in name) # a name içinde yok mu diye soruyoruz.

print('e' in name)
