website = "wwW.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
# 4- 'website' içinde kaç tane a karakteri vardır? (count(a))
# 5- 'website' www ile başlayıp com ile bitiyor mu?
# 6- 'website' içinde .com ifadesi var mı?
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isAlpha, isDigit) 
# 8- 'contonents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

# Cevaplar
# 1-' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

#message = 'Hello World'
#message = message.strip() # message = 'Hello World'.strip olarakda yazılabilir. lstrip soldan siler rstrip ise sağdan siler.  
#print(message)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

# message = 'www.sadikturan.com'
# message = message.lstrip('www.')
# message = message.rstrip('.com')
# print(message)

# yada

# message = 'www.sadikturan.com'
# message = message.strip('w.moc')
# print(message)

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

#course = course.lower()
#print(course)

#course = course.title()  sadece baş harfler büyük
#course = course.upper() tamamı büyük harf

# 4- 'website' içinde kaç tane a karakteri vardır?

# website = website.count('a') 
# print(website)

# yada

# website = website.count('a') a yı o indeksi ile 10 indeksi arasında arasın

# 5- 'website' www ile başlayıp com ile bitiyor mu?

# isFound = website.startswith('WWW') 
# print(isFound)
# isFound = website.endswith('com')
# print(isFound)

# 6- 'website' içinde .com ifadesi var mı?

# isFound = website.find('.com') # soldan saymaya başlar rfind ise sağdan saymaya başlar
# isFound = website.rfind('.com') # sağdan saymaya başlar
# isFound = website.index('.com') # Şeklinde de arama yapılabilir. # find da aranan kelime bulunamadığında -1 dönmekte iken index de hata dönemktedir. 
# print(isFound)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isAlpha, isDigit) 

# course = course.isalpha() # hepsi harf mi diye sorar isDigit ise hepsi rakam mı diye sorar
# print(course)


# 8- 'contonents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# message = 'contonents'
# message = message.center(50, '*') 
# message = message.ljust(50, '*') # content karakter dizisini sola yaslar
# message = message.rjust(50, '*') # content karakter dizisini sağa yaslar
# print(message)

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

# course =course.replace(' ', '-')
# print(course)


# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

# message = 'Hello World'
# message = message.replace('World', 'There')
# print(message)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

# course = course.split(' ')
# print(course)