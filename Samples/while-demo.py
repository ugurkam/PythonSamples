from unicodedata import name


sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesini while ile ekrana yazdırınız.

# i = 0

# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# print('bitti')







# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırınız.

# start = int(input('Baslangıc sayısı giriniz: '))
# finish = int(input('Bitis sayısı giriniz: '))

# i = start

# while i < finish:
#     i += 1
#     if i % 2 == 1:    
#         print(i)

# print('Bitti')

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırınız.

# x = 100

# while x > 1:
#     print(x)
#     x -= 1
    

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.

# numbers = []
# x = 0

# while x < 5:
#     num = int(input('Bir sayı giriniz: '))
#     numbers.append(num)
#     x += 1
# numbers.sort()
# print(numbers)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.

#    ** ürün sayısını kullanıcıya sorun.

#    ** dictionary listesi yapısı (name, price) şeklinde olsun.

#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


# urunler = []

# adet = int(input('Urun Sayısı Kac Olsun: '))
                 
# i = 0

# while i< adet:
#     name = input('urun ismi: ')
#     price = int(input('urun fiyatı: '))
#     urunler.append({
#         'name': name,
#         'price': price
#     }) 
    
#     i += 1
    
# for urun in urunler:
#     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')
    
# print(urunler)


# for urun in urunler:
#     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')