


list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e', ]
list3 =  [100, 200, 300, 400, 500]

print(list(zip(list1, list2, list3)))

# Çıktısı

# [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

# for list in zip(list1, list2, list3):
#     print(list)

# Çıktısı


# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
# (4, 'd', 400)
# (5, 'e', 500)

# for a,b,c in zip(list1, list2, list3):
#     print(a)
    
# Çıktısı:
    
# 1
# 2
# 3
# 4
# 5

for a,b,c in zip(list1, list2, list3):
    print(a,b)

# Çıktısı:

# 1 a
# 2 b
# 3 c
# 4 d
# 5 e