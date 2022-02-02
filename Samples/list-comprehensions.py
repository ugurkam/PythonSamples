# from traceback import print_tb


# numbers = []

# for x in range(10):
#     numbers.append(x)
# print(numbers)

# Çıktısı:
    
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  

# yada aşağıdaki şekilde de yazılabilir

# numbers = [ x for x in range(10)] # for x in range(10) ile 0'dan 10'a kadar sayıları tek tek alıyor ve baştaki x'e atıyor x'in içindeki değer dizinin içindeki elemanları temsil ediyor.

# print(numbers)


# Çıktısı:
    
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  


# for x in range(10):
#     print(x **2) # her aşamada sayıların üssü alınır.
    

# Çıktısı:
    
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
    
# Aşağıdaki şekilde de yazabiliriz


# numbers = [ x **2 for x in range(10)]
# print(numbers) 

# Çıktısı:

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# numbers = [x*x for x in range(10)]
# print(numbers)

# Çıktısı:
    
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# numbers = [x*x for x in range(10) if x % 3 == 0 ] # Eğer bulduğu x sayısının karesinden 3'e tam bölünen var ise sadece onlar yazılsın.
# print(numbers)

# Çıktısı:
    
# [0, 9, 36, 81]


# myString = 'Hello Ugur'
# myList = []

# for letter in myString:
#     myList.append(letter)
    
# print(myList)

# Çıktısı:
    
# ['H', 'e', 'l', 'l', 'o', ' ', 'U', 'g', 'u', 'r']

# yada böyle yazılabilir

# myList = [letter for letter in myString]
# print(myList)

# Çıktısı:
    
# ['H', 'e', 'l', 'l', 'o', ' ', 'U', 'g', 'u', 'r']

# years = [1983, 1999, 2008, 1956, 1986]

# ages = [(2019 - year) for year in years]
# print(ages)

# Çıktısı:
    
# [36, 20, 11, 63, 33]




# from unittest import result


# result = [x if x%2==0 else 'tek' for x in range(1,10)] # for x in range ile 1'den ona kadarı sayıları alıyor sonra sayıyı en bastaki x'in içine koyuyor dize'ye eklemeden önce if ve else komutuna bakıyor ıf'e uyanları yazıyor uymayanları ise belirtilen kelimeyi yazıyor
# print(result)

# result = []

# for x in range(3):
#     for y in range(3): 
#         result.append((x,y)) # Appende içine bir obje alabildiğinden parantez içine alınarak x ve y bir obje olarak kabul edildi.

# print(result) # ilk önce ilk for a girer x 0 ikinci fora girer y 0 (0,0) yazar ikinci for y 1 x 0 bu durumda (0,1) yazar ikinci forda y 2 x 0 (0,2) yazar fordan çıkar ilk for girer x 1 ikinci for girer y 0 bu durumda (1,0) yazar  


# Çıktısı:

# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# yada aşağıdaki şekilde yazılabilir.

# numbers = [(x,y) for x in range(3) for y in range(3)]  

# print(numbers)



# Çıktısı:

# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# numbers = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]  

# print(numbers)

# Çıktısı:
    
# [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 
# 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]