
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]


# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
# 2-  "Sena" değerini listenin başına ekleyiniz.
# 3-  "Deniz" ismini listeden siliniz.
# 4-  "Deniz" isminin indeksi nedir ?
# 5-  "Ali" listenin bir elemanı mıdır ?
# 6-  Liste elemanlarını ters çevirin.
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# 11- years dizisinde kaç tane 1998 değeri vardır ?
# 12- years dizisinin tüm elemanlarını siliniz.
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

# Cevaplar

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.

names.append('Cenk')
print(names)

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
print(names)

# 3-  "Deniz" ismini listeden siliniz.

# names.remove('Deniz')
# print(names)

# 4-  "Deniz" isminin indeksi nedir ?

result = names.index('Deniz')
print(result)

# 5-  "Ali" listenin bir elemanı mıdır ?

result = 'Ali' in names
print(result)

# 6-  Liste elemanlarını ters çevirin.

names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = 'Chevrolet,Dacia'
newList= str.split(',')
print(newList)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?


min = min(years)
max = max(years)

print(min, max)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input('Marka: ')
markalar.append(marka)

marka = input('Marka: ')
markalar.append(marka)

marka = input('Marka: ')
markalar.append(marka)
 
print(markalar)

