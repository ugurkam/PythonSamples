sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3' ün katıdır ?

# for num in sayilar:
#     if num % 3 == 0:
#         print(num)
        
# Çıktı:
    
# 3
# 9
# 12
# 21

# 2- Sayilar listesinde sayıların toplamı kaçtır ?

# toplam= 0

# for num in sayilar:
#     toplam += num
# print(toplam)


# 3- Sayilar listesindeki tek sayıların karesini alınız.

# for num in sayilar:
#     if num % 2 == 1:
#         print(num **2)

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# for city in sehirler:
#     if len(city) <= 5:
#         print(city) 

# 5- Ürünlerin fiyatları toplamı nedir ?

urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]

# toplam = 0

# for urun in urunler:

#     fiyat = (int(urun['price'])) # ulaşmak istediğimiz value'nin key ini yazıyoruz.
#     toplam += fiyat
# print(toplam)
    

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])