# 1- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol eden python uygulamasını yapınız.

# sayı = int(input('Bir sayı giriniz: '))

# if sayı < 0:
#     print('Girilen sayı negatiftir')

# elif sayı > 0:
#     if ((sayı % 2) == 0):
#         print('Girilen sayı pozitif çift sayıdır')
#     else:
#         print('Girilen Sayı pozitif tek sayıdır')
        
# elif sayı == 0:
#     print('Girilen sayı sıfırdır')

    

# 2- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'ugurkam@gmail.com'
# password = '1234'

# girilenEmail = input('eposta giriniz: ')
# girilenPassword = input('parola giriniz: ')

# if (girilenEmail == email):
#     if (girilenPassword == password):
#         print('Giris basarılı')
#     else:
#         print('parola hatalı')
# else:
#     print('eposta hatalı')


# 3- Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.


# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if (a > b) and (a > c):
#     print('a en buyuk sayıdır.')

# elif (b > a) and (b > c):
#     print('b en buyuk sayıdır.')

# elif (c > a) and (c > b):
#     print('c en buyuk sayıdır.')
    
# elif ( a == b) and (b == c):
#     print('sayılar birbirine esittir.')

# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayan python uygulamasını yapınız.

# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.


# vize1 = int(input('Vize 1: '))
# vize2 = int(input('Vize 2: '))
# final = int(input('final: '))

# ortalama = ((vize1 + vize2)/2 * 0.60) + final * 0.40
# print(ortalama)

# if final >= 70:
#     print(f'ogrencinin ortalaması {ortalama} ve gecme durumu basarılı')

# elif (ortalama >= 50) and (final >= 50):
#     print(f'ogrencinin ortalaamsı {ortalama} ve gecme durumu basarılı')
    
# else:
#     print(f'ogrencinin ortalaması {ortalama} ve gecme durumu basarısız ')


# 5- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayan python uygulamasını yapınız.

# Formül: (Kilo / boy uzunluğunun karesi)

# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)


ad = input('Ad: ')
soyad = input('Soyad: ')
kilo = float(input('Kilo: '))
boy = float(input('Boy: '))

index = (kilo / (boy **2))

if (index >= 0) and (index < 18.5):
    print(f'{ad} kilo indeksin: {index} ve kilo degerlendirmen zayıf')

elif (index >= 18.5 ) and (index < 25.0):
    print(f'{ad} kilo indeksin: {index} ve kilo degerlendirmen normal')
    
elif (index >= 25.0 ) and (index < 30.0):
    print(f'{ad} kilo indeksin: {index} ve kilo degerlendirmen fazla kilolu')
    
elif (index >= 30.0 ) and (index < 35.0):
    print(f'{ad} kilo indeksin: {index} ve kilo degerlendirmen obez')
    
else:
    print(f'bilgileriniz yanlıs')

