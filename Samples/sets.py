fruits = {'portakal', 'elma', 'muz'}

print(fruits)

for x in fruits:
    print(x)
    
    
# Fruits setine eleman eklemek için    
fruits.add('karpuz')
fruits.update(['kavun', 'visne'])

print(fruits)

myList = [1,3,5,7,1,4,3,8]

print(myList)
print(set(myList))

# Fruits setinden eleman silmek için

#fruits.remove('karpuz')
#fruits.discard('kavun')

#fruits.pop() # son elemanı siler ancak sıralı bir liste olmayıp karışık olduğundan son elemanın ne olduğu ve silineceği garanti edilemez.

fruits.clear () # tüm elemanlar silinir
print(fruits)  