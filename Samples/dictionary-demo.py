# ogrenciler = {
#         '120': {
#             'ad': 'Ali',
#             'soyad': 'Yılmaz',
#             'telefon': '532 000 00 01'
#         },
#         '125': {
#             'ad': 'Can',
#             'soyad': 'Korkmaz',
#             'telefon': '532 000 00 02'
#         },
#         '128': {
#             'ad': 'Volkan',
#             'soyad': 'Yükselen',
#             'telefon': '532 000 00 03'
#         },
#     }

# print(ogrenciler['120'])

# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

# ** Henüz döngüleri görmediğimizden dolayı input() ile bilgi alma işlemini 3 öğrenci için tekrarlayabilirsiniz.


# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.




ogrenciler = {}
number = input('Ogrenci No:')
name = input('Ogrenci Adı:')
surname = input('Ogrenci Soyad:')
phone = input('Ogrenci Telefon:')

ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}


number = input('Ogrenci No:')
name = input('Ogrenci Adı:')
surname = input('Ogrenci Soyad:')
phone = input('Ogrenci Telefon:')

ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}


number = input('Ogrenci No:')
name = input('Ogrenci Adı:')
surname = input('Ogrenci Soyad:')
phone = input('Ogrenci Telefon:')

ogrenciler.update ({
    number : {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}
})
 
print(ogrenciler)




 

ogrno = input('ogrenci no:')
ogrenci = ogrenciler[ogrno]
print(f"aradıgınız {ogrno} nolu ogrencinin adı : {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")