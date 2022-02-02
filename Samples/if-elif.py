# x = int(input('x: '))
# y = int(input('y: '))

# if x > y:
#     print("x y'den buyuktur")

# elif x ==y:
#     print("x y'ye esit")

# else:
#     print("y x'den buyuktur")

from traceback import print_tb


num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')

elif num < 0:
    print('sayı negatif')

else:
    print("sayı 0")
    