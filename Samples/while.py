# 0 - 100 e kadar

x = 0

# while x < 10:  # x = 0, sonra x'i yazıyor devamında x'i 1 ile topluyor x = 1 oluyor devamında x 10'dan küçük mü diye bakıyor küçük ise tekrar x'i yazdırıyor 
# # sonrasında x'i 1 ile topluyor x=2 oluyor. x 10'dan küçük olmadığında while false değer veriyor ve dışardaki print'i yazdırıyor
    
#     print(x)
#     x += 1
    
# print('Bitti') 



# while x < 10:  # x = 0, sonra x'in mod 2 kalanına bakıuor kalan 1'e eşit ise if'in içine girip x'i yazıyor devamında x'i 1 ile topluyor x = 1 oluyor devamında x 10'dan küçük mü diye bakıyor 
# # küçük ise tekrar x 'in mod 2 kalanına bakıyor kalan 1'e eşit ise x'i yazdırıyor sonrasında x'i 1 ile topluyor x=2 oluyor. x 10'dan küçük olmadığında while false değer veriyor ve dışardaki print'i yazdırıyor
#     if x % 2 == 1:
#         print(x)
#     x += 1
    
# print('Bitti')


# x = 0

# while x < 10:
#     if x % 2 ==1:
#         print(f'Sayı tek: {x}')
#     else:
#         print(f'Sayı cift: {x}')
    
#     x += 1

# print('Bitti')




# ORNEK


name = ''       # false

while not name: # name boş olduğu surece (kastedilen boşluk değil hiç birşey girilmemesi) devam et. name girildiğinde dolmuş olacak while'dan çıkacak.
    name = input('isim giriniz: ')
    
print(name)
