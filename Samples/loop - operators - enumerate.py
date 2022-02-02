


# from distutils.archive_util import make_archive
# from operator import index


# greeting = 'Hello There'

# for letter in greeting:
#     print(letter)
    
    
# İndex numaralarına ulaşmake_archive

# greeting = 'Hello There'
# index = 0


# for letter in greeting:
#     print(f'index: {index} letter: {letter} ')
#     index += 1

# Çıktısı:
    
# index: 0 letter: H 
# index: 1 letter: e 
# index: 2 letter: l 
# index: 3 letter: l 
# index: 4 letter: o
# index: 5 letter:
# index: 6 letter: T
# index: 7 letter: h
# index: 8 letter: e
# index: 9 letter: r
# index: 10 letter: e
    
# yada

# greeting = 'Hello There'
# index = 0


# for letter in greeting:
#     print(f'index: {index} letter: {greeting[index]} ')
#     index += 1

# Çıktısı:
    
# index: 0 letter: H 
# index: 1 letter: e 
# index: 2 letter: l 
# index: 3 letter: l 
# index: 4 letter: o
# index: 5 letter:
# index: 6 letter: T
# index: 7 letter: h
# index: 8 letter: e
# index: 9 letter: r
# index: 10 letter: e


# Enumerate ##### index tanımlamadan index yazırma

# greeting = 'Hello There'

# for letter in enumerate(greeting):
#     print(letter)


# Çıktısı
    
# (0, 'H')
# (1, 'e') 
# (2, 'l') 
# (3, 'l') 
# (4, 'o') 
# (5, ' ') 
# (6, 'T') 
# (7, 'h') 
# (8, 'e') 
# (9, 'r') 
# (10, 'e')



# greeting = 'Hello There'

# for index, letter in enumerate(greeting):
#     print(f'index: {index} letter: {letter} ')
#     index += 1
    
# Çıktısı

# index: 0 letter: H 
# index: 1 letter: e  
# index: 2 letter: l  
# index: 3 letter: l  
# index: 4 letter: o  
# index: 5 letter:    
# index: 6 letter: T  
# index: 7 letter: h  
# index: 8 letter: e  
# index: 9 letter: r  
# index: 10 letter: e 


# greeting = 'Hello There'

# for index, letter in enumerate(greeting):
#     print(f'index: {index} letter: {letter} ')
    
    