# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)

#    ** "random modülü" için "python random" şeklinde arama yapın.

#    ** 100 üzerinden puanlama yapın. Her soru 20 puan.

#    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.


# import random

# number = random.randint(1, 1)
# life = int(input('Oyuncu hakki giriniz: '))
# hak = life
# counter = 0

# while hak > 0:
#     hak -= 1
#     counter += 1
#     guess = int(input('Tahmin edilen sayi: '))
    
#     if number == guess:
#         print(f'Tebrikler {counter} defada bildiniz. Toplam puaniniz {100 / life * (life -counter)}')
#         break
    
    
    
#     elif number > guess:
#         print('Yukari')
        
#     elif number < guess:
#         print('Asagi')
    
#     if hak == 0:
#         print('Hakkiniz bitti.')
        
        

import random

number = random.randint(1, 1)
life = int(input('Oyuncu hakki giriniz: '))
hak = life
counter = 0

while hak > 0:
    
    guess = int(input('Tahmin edilen sayi: '))
    
    if number == guess:
        print(f'Tebrikler {counter} defada bildiniz. Toplam puaniniz {100 - (counter * (100 / life))}')
        break
        
    elif number > guess:
        print('Yukari')
        
    elif number < guess:
        print('Asagi')
    
    if hak == 0:
        print('Hakkiniz bitti.')
        
    hak -= 1
    counter += 1
    