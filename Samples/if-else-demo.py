# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol eden python uygulamasını yapınız.

# ** Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# name = input('isim: ')

# age = int(input('yas: '))
          
# graduate = input('Lise mi Universite mi: ')

# if (age >= 18): 
#     if ((graduate == 'lise' or graduate == 'universite')):
#        print('ehliyet alabilirsiniz')
    
#     else:
#        print('ehliyet alaamzsınız egitim durumunuz tutmuyor')

# else:
#     print('ehliyet alamazsınız yasınız tutmuyor')


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdıran python uygulamasını yapınız.

# 0 -24 => 0

# 25-44 => 1

# 45-54 => 2

# # 55-69 => 3

# # 70-84 => 4

# # 85-100 => 5

# exam1 = float(input('1. yazılı: '))
# exam2 = float(input('2. yazılı: '))
# quiz = float(input('sozlu: '))

# ortalama = (exam1 + exam2 + quiz)/3

# if (ortalama>=0) and (ortalama < 25):
#     print(f'ortalamanız: {ortalama} notunuz 0')

# elif (ortalama>= 25) and (ortalama < 45):
#     print(f'ortalamanız: {ortalama} notunuz 1')
    
# elif (ortalama >= 45) and (ortalama < 55):
#     print(f'ortalamanız: {ortalama} notunuz 2')
    
# elif (ortalama >= 55) and (ortalama < 70):
#     print(f'ortalamanız: {ortalama} notunuz 3')

# elif (ortalama >= 70) and (ortalama < 85):
#     print(f'ortalamanız: {ortalama} notunuz 4')
    
# elif (ortalama >= 85) and (ortalama <=100):
#     print(f'ortalamanız: {ortalama} notunuz 5')
        
# else:
#     print('yanlıs girdiniz')


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayan python uygulamasını yapınız.

# 1. Bakım => 1. yıl

# 2. Bakım => 2. yıl

# 3. Bakım => 3. yıl

# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..

# *** datetime modülünü kullanmanız gerekiyor. (simdi) - (2018/8/1) => gün

# import datetime


# tarih = input('Aracınızın trafige hangi tarihte cıktı ornek (2019/8/9):')
# tarih = tarih.split('/')

# trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

# now = datetime.datetime.now()
# fark = now - trafigeCikis
# days = fark.days

# if (days <= 365):
#     print('1. servis aralığı')
    
# elif (days > 365) and (days < 365 * 2 ):
#     print('2. servis bakım aralıgı')

# elif (days > 365*2) and (days < 365 * 3 ):
#     print('3. servis aralıgı')
    
# else:
#     print('hatalı sure')



