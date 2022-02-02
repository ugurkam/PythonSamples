# MAP Metodu


# def square(num):
#     return num ** 2

# result = square(2)
# print(result)

# Çıktısı:

# 4

# Boyle de yazılabilir:

# def square(num): return num ** 2

# result = square(2)
# print(result)

# Çıktısı:

# 4

 # Elimizde olan bir listenin karesini alıp ekrana yazdırmak istersem

# def square(num):
#         return num ** 2



# liste = [1, 3, 5, 9]

# for i in liste:
#     result = square(i)
#     print(result)

# Çıktısı:

# 1
# 9
# 25
# 81


# Yada soyle de yazılabilir: MAP Metodu ile yani.

# def square(num):
#         return num ** 2

# liste = [1, 3, 5, 9]

# result = list(map(square, liste)) # Map metodu burada liste ile cevrilmektedir.
# print(result)

# Çıktısı:

# [1, 9, 25, 81]


# Alternatif olarak boyle de yazılabilir:

# def square(num):
#         return num ** 2

# liste = [1, 3, 5, 9]

# for item in map(square, liste):
#     print(item)

# Çıktısı:
    
# 1
# 9
# 25
# 81


# !!!!! Önemli olan map metodunun ya bir liste ile çevrili olması yada for metodu ile elemanları üzerinden dönülmesi gerekiyor.




# LAMBDA Metodu



# liste = [1, 3, 5, 9]

# result = list(map(lambda num: num ** 2, liste)) 

# print(result)

# Çıktısı:

# [1, 9, 25, 81]


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BOYLEDE YAZILABİLİR

# square = lambda num: num ** 2

# liste = [1, 3, 5, 9]

# result = list(map(square, liste))

# print(result)

# Çıktısı:
    
# [1, 9, 25, 81]


# !!!!!!!!!!!!!!!!!!!!!!! Böyle de yazılabilir !!!!!!!!!!!!!!!

# square = lambda num: num ** 2

# result = square(5) # 5 'in karesini alır

# print(result)



# --------------------------------------------- FILTER -------------------------------------------------------------

 
# def check_even(num):
#     return num % 2 == 0 # Çift olan sayıları true olarak döner
 
# liste = [1, 3, 5, 9,10,20,40,50]

# result = list(filter(check_even, liste))
# print(result) 

# Çıktısı:
    
# [10, 20, 40, 50]



# ------------------------- Lamba ile yaparsak

 
# liste = [1, 3, 5, 9,10,20,40,50]

# result = list(filter(lambda num: num % 2 == 0, liste))
# print(result) 

# Çıktısı:
    
# [10, 20, 40, 50]



# Yada Boylede yazılabilir

# liste = [1, 3, 5, 9,10,20,40,50]

# check_even = lambda num: num % 2 == 0

# result = check_even(liste[3])

# print(result)

# Çıktısı:
 
#  False   
    
# 3. index tek olduğu için false gönderir

# liste = [1, 3, 5, 9,10,20,40,50]

# check_even = lambda num: num % 2 == 0

# result = check_even(liste[5])

# print(result)

# # Çıktısı:
 
# #  True   
    
# # 5. index çift olduğu için true gönderir
