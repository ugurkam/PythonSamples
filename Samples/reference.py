# Value types => string, numbers (float, int)

# x = 5
# y = 25

# x = y

# y = 10

# print(x,y)


# Reference types => list, class sadece adresler atanıyor içindeki değerler değil bu durumda da 500 sayılı bir liste var tamamını kopyalamak yerine sadece adresi alınıyor.

a = ['elma', 'armut', 'karpuz']

b = ['erik', 'armut', 'karpuz']


a = b

b[0] = 'kavun'

print(a,b)