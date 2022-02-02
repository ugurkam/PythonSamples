website = "http://wwW.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisindeki kaç karakter bulunmaktadır.
# 2- 'website' içinden www karakterlerini alın.
# 3- 'website' içinden com karakterlerini alın.
# 4- 'course' içinden ilk 15 ve son 15 karakteri alın.
# 5- 'course' içindeki karakterleri tersden yazdırın.

name, surname, age, job, = 'bora', 'yılmaz', 32, 'muhendis'


# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis'

# 7- 'Hello world' ifadesindeki w harfini W ile değiştirin.

x = 'Hello world'
x.replace('w', 'm')
# 8- 'abc' ifadesini yan yana 3 defa yazdırın

s = 'abc'

# Cevaplar

# 1
length = len(course)
print(length)

# 2
print(website[7:10])

# 3
print(website[-3:])

# 4
print(course[0:15])
print(course[length-15:])

# 5

print(course[::-1])

# 6

print('Benim adım {} {}, yaşım {} ve mesleğim {}'.format(name, surname, age,job))

# 7
print(x)

# 8

print(s*3)