# def sayHello():
#     print('Hello Ugur')
    
# sayHello()

# Çıktısı:
    
# Hello Ugur

# yada böyle de yazılabilir

# def sayHello(name):
#     print('Hello ' + name)
    

# ad = 'ugur'   
# sayHello(ad)

# Çıktısı:

# Hello ugur




# def sayHello(name = 'User'):
#     print('Hello ' + name)
    
  
# sayHello() # parametre gönderilmediğinde user'ı yazar gönderildiğinde ise gönderileni yazar

# Çıktısı:

# Hello User

# Gönderildiğinde:
    
# def sayHello(name = 'User'):
#     print('Hello ' + name)
    
  
# sayHello('Ahmet') # parametre gönderilmediğinde user'ı yazar gönderildiğinde ise gönderileni yazar

# Çıktısı:

# Hello Ahmet
    



# def sayHello(name = 'user'):
#     return 'Hello ' + name

# msg = sayHello('taso')

# print(msg)

# Çıktısı:
    
# Hello taso


# def total(num1, num2):
#     return num1 + num2

# result = total(10, 11)

# print(result)

# Çıktısı:
    
# 21



def yasHesapla(dogumYili):
    return 2021 - dogumYili

result = yasHesapla(1985)

print(result)

# Çıktısı:
    
# 36


# def emeklilikHesapla (dogumYili, name):
#     age = yasHesapla(dogumYili) # yas Hesapla fonksiyonunu emeklilik Hesapla fonksiyonu içinde kullandık. 
#     emeklilik = 65 - age
    
#     if emeklilik > 0:
#         print(f'{name}in emekliliğe {emeklilik} yili kaldı')
    
#     else:
#         print('Zaten Emeklisiniz.')
    

# emeklilikHesapla(1985, 'ugur')





def emeklilikHesapla (dogumYili, name):
    '''
    DOCSTRING: dogum yiliniza göre ememkliliginizr kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil
       
    
    '''
        
    age = yasHesapla(dogumYili) # yas Hesapla fonksiyonunu emeklilik Hesapla fonksiyonu içinde kullandık. 
    emeklilik = 65 - age
    
    if emeklilik > 0:
        print(f'{name}in emekliliğe {emeklilik} yili kaldı')
    
    else:
        print('Zaten Emeklisiniz.')
    

emeklilikHesapla(1985, 'ugur')


# bir fonksiyonunun nasıl kullanılacağını 

# print(help(print)) ile ogrenebiliriz 

# örnek:

# print(help(emeklilikHesapla)) 

# Çıktısı:

# emeklilikHesapla(dogumYili, name)
#     DOCSTRING: dogum yiliniza göre ememkliliginizr kac yil kaldi
#     INPUT: Dogum yili
#     OUTPUT: Hesaplanan yil


# ornek 2:

# print(help(list.append))

# Çıktısı:
    
# append(self, object, /)
#     Append object to the end of the list.