list = [1, 2, 3]

tuple = (1, 'iki', 4)

print(type(list))
print(type(tuple))

print(list[1])
print(tuple[1])


print(len(list))
print(len(tuple))

list = ['ali', 'veli', 'deli']
tuple = ('ahmet', 'mehmet', 'ayse')
tuple2 = ('ahlem', 'mahmet', 'aysi') + tuple

list[0] = 'kamil'
#  tuple[0] = 'halim' # Tuple değiştirilemez liste değiştirilebilir. Değiştirilmesini istemediğim bilgiler için tuplu kullanırız.

print(list)
print(tuple2)
