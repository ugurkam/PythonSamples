# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız. Formül: (Kilo / boy uzunluğunun karesi)

# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

# 0-18.4 => Zayıf

# 18.5-24.9 => Normal

# 25.0-29.9 => Fazla Kilolu

# 30.0-34.9 => Şişman (Obez)

# Cevaplar

# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# number = int(input('Bir Sayı Giriniz: '))
# result = (number > 0 ) and (number < 100)
# print(f'Girilen sayı: {number}, 0 ile 100 arasındadır. {result}')


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# number = int(input(' Bir sayı giriniz: '))
# result = (number > 0) and (number % 2 == 0)
# print(f'Girilen sayı: {number}, Pozitif bir çift sayıdır. {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'ugur.kam@gmail.com'
# password = int('19851985')

# eposta = input('eposta giriniz: ')
# parola = int(input('parola giriniz: '))

# # result = (email == eposta) and (password == parola)
# # print(f'Girilen eposta: {eposta}, parola: {parola} doğrudur. {result}')


# # 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# resulta = (a > b) and (a > c)
# print(f'a en büyük sayıdır: {resulta}')

# resultb = (b > a) and (b > c)
# print(f'b en büyük sayıdır: {resultb}')

# resultc = (c > a) and (c > b)
# print(f'c en büyük sayıdır: {resultc}')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# from operator import index


# vize1 = int(input('vize1: '))
# vize2 = int(input('vize2: '))
# final = int(input('final: '))

# ortalama = ((vize1 + vize2)/2 * 0.60) + (final * 0.40)
# resulta = (ortalama>= 50) and (final > 50)
# print(f'ogrencinin ortalaması: {ortalama} gecme durumu {resulta}')

# resultb = (ortalama>= 50) or (final >= 70)
# print(f'ogrencinin ortalaması: {ortalama} gecme durumu {resultb}')


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız. Formül: (Kilo / boy uzunluğunun karesi)

# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

# 0-18.4 => Zayıf

# 18.5-24.9 => Normal

# 25.0-29.9 => Fazla Kilolu

# 30.0-34.9 => Şişman (Obez)

name = input('ad: ')
kilo = float(input('kilo: '))
boy = float(input('boy: '))
index = (((kilo) /(boy ** 2)))

zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
kilolu = (index >= 25.0) and (index <= 29.9)
obez = (index >= 30.0) and (index <= 34.9)

print(f'{name} kilo endeksin: {index} kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo endeksin: {index} kilo değerlendirmen bormal: {normal}')
print(f'{name} kilo endeksin: {index} kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo endeksin: {index} kilo değerlendirmen obez: {obez}')