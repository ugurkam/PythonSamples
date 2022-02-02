# numbers = [1, 2, 3, 4, 5]

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])


# for döngüsü ile

# for num in numbers: # listenin eleman sayısı kadar for döngüsü dönmektedir.
#     print(num) # yapılan işlem her for döngüsünde numbers dan elemanı al num içine at ve ekrana yaz.
    
    
# for num in numbers: # listenin eleman sayısı kadar for döngüsü dönmektedir.
#     print('Hello') # yapılan işlem her for döngüsünde numbers dan elemanı al num içine at ve ekrana yaz. listenin eleman sayısı kadar ekrana hello yazar. her dönüşte başka bir işlem yaptırılabilir.
    
    
    
# çıktısı:
    
# Hello
# Hello
# Hello
# Hello
# Hello

# LİSTE:

# names = ['ugur', 'ufuk', 'burcak', 'taso']

# for name in names:
#     print(f'my name is {name}')
    
# çıktısı;

# my name is ugur
# my name is ufuk
# my name is burcak
# my name is taso


# name = 'ugur kam'

# for n in name:
#     print(n)

# Çıktısı:
    
# u
# g
# u
# r

# k
# a
# m


# TUPLE:

# tuple = (1,2,3,4,5,6)

# for t in tuple:
#     print(t)
    
# tuple'ın çıktısı:

# 1
# 2
# 3
# 4
# 5
# 6


# tuple = [(1,2), (3,4), (5,6), (7,8), (9,0) ]

# for t in tuple:
#     print(t)
    
# çıktısı:
    
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)
# (9, 0)


# tuple = [(1,2), (3,4), (5,6), (7,8), (9,0) ]

# for a,b in tuple:
#     print(a)
    
# Çıktısı:  sadece tuple'ın ilk elemanlarını yazar
       
# 1
# 3
# 5
# 7
# 9

# tuple = [(1,2), (3,4), (5,6), (7,8), (9,0) ]

# for a,b in tuple:
#     print(a,b)
    
# çıktısı: ilk ve ikinci elemanlarını yazar
    
# 1 2
# 3 4
# 5 6
# 7 8
# 9 0


# DİCTİONARY : KEY, VALUE



# d = {'k1': 6, 'l2': 7, 'm3': 8, 'n4': 9}

# for item in d:
#     print(item) 
    
# Çıktısı: dictionary'de sadece key bilgileri gelir
    
# k1
# l2
# m3
# n4

# d = {'k1': 6, 'l2': 7, 'm3': 8, 'n4': 9}

# for item in d.items(): # elemen gruplarına ulaşmak için d.items() yazılmalı
#     print(item) 
    
# Çıktısı:
    
# ('k1', 6)
# ('l2', 7)
# ('m3', 8)
# ('n4', 9)


# d = {'k1': 6, 'l2': 7, 'm3': 8, 'n4': 9}

# for key, value in d.items(): # elemen gruplarına ulaşmak için d.items() yazılmalı
#     print(key) 


# Çıktısı:
    
# k1
# l2
# m3
# n4


# d = {'k1': 6, 'l2': 7, 'm3': 8, 'n4': 9}

# for key, value in d.items(): # elemen gruplarına ulaşmak için d.items() yazılmalı
#     print(key, value) 
    
# Çıktısı:
    
# k1 6
# l2 7
# m3 8
# n4 9

