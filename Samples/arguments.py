# def changeName(n):
#     n = 'ada'

# name = 'leyla'

# changeName(name)

# print(name)

# Çıktısı:

# leyla

# Value type olduğu için fonksiyonun dışındaki bir değişken değiştirlemiyor




def change(k):
    k[0] = ['istanbul']

cities = ['ankara', 'izmir']

change(cities)

print(cities)

# Çıktısı:

# ['istanbul', 'izmir',]


# Fonkiyon çağrılınca sehirler listesi methoda gidiyor ve 0 ınci indexi istanbul olarak değiştiriliyor.

# Burada yukarıdaki ilk işlemde yapıldığı value typelardan farklı olarak referans kopyalaması yapılıyor

# yani burada tanımlanan k parametresine tanımlamış olduğumuzu sehirler dizisinin adresi gönderiliyor ve bu adresteki bilginin 0 ıncı indeksindeki değeri 'istanbul' yap diyoruz.

# Dışarıda tanımlanan dizinin ilk elemanı değiştiriliyor.

# Burada cities dizisinin bir kopyası çıkartılmıyor orjinal dizinin listesi gönderiliyor ve o adresti bilgi güncelleniyor.






# def add(a,b): # a ve b yazdığımız için sadece iki tane parametre gönderilebilir 3. gönderilirse yada 1 tane gönderilirse hata verir
#     return sum((a,b))

# print(add(10,20))



# def add(a,b, c=0, d=0, e=0): # c=0, d=0, e=0  yazarak kaç tane parametre göndereceğimi bilmediğim durumlarda sorun çözülebiir.
#     return sum((a,b))

# print(add(40,50))

# def add(*params): # * oarams ile istediğimiz kadar ( ister 1 ister 100 ) parametre gönderebiliriz. params öncelikle argümanları bir liste yapar sonra toplar return öncesine print ile paramsı yazdırarak görebiliriz. params[0] ile de istediğimiz elemana ulaşabilir.z

#     print(type(params)) # olmasa da olur sadece gönderdiğimiz parametreleri görmek için kullanabiliriz.


#     print(params) # olmasa da olur sadece gönderdiğimiz parametreleri görmek için kullanabiliriz.

#     return sum((params))

# print(add(10,20,30))


# Çıktısı: Tuple bir çıktı

# (10, 20, 30)
# 60



# SUM fonksiyonunu kullanmak istemezsek

# def add(*params):
#     sum = 0
    
#     for n in params:
#         sum = sum + n
    
#     return sum

# print(add(10,20)) 

# toplam bilgisini alırız.

# Çıktısı:
    
# 30


# # FONKSİYONA GÖNDERİLEN VERİLER BİR VERİ TİPİ OLSA

# # 1. Kullanıcı adı 2. Yaşadığı yer 3. maaş bilgişi şeklinde olsa ve sayısı belli değilse.

# Bu bilgiler dictionary'de tutulur.

# def displayUser(**arguments):
   
#     for key, value in arguments.items():
#         print(f'{key} is {value}')

# displayUser( name = 'ugur', age = 36, city = 'prague')
# displayUser( name = 'burcak', age = 30, city = 'holesovice', phone = '111')
# displayUser( name = 'taso', age = 1, city = 'stroöovka', phone = '222', email = 'tasokam@gmail.com')


# Çıktısı: Çıktı dictionary olarak gelir.
    
# name is ugur
# age is 36
# city is prague
# name is burcak
# age is 30
# city is holesovice
# phone is 111
# name is taso
# age is 1
# city is stroöovka
# phone is 222
# email is tasokam@gmail.com


def myFunc(a, b, *params, ** args):
    print(a)
    print(b)
    print(params)
    print(args)
    
myFunc(10,20, 30, 40, 50, key = 'ugur', value = 'burcak' )