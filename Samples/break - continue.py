# name = 'ugur kam'

# for letter in name:
#     if letter == 'k': # 'K' harfine geldiğinde continue komutu ile alttaki kod'a geçmeden baştan for döngüsüne girer
#         continue
#     if letter == 'm': 
#         break
#     print(letter)



# x = 0

# while x < 5:
#     if x == 3:
#         break
#     print(x)
#     x += 1


# x = 0

# while x < 5:
#     if x == 3:
#         continue
#     print(x)
#     x += 1 # x + 1 aşağıda kaldığı ve x 2 iken döngüden çıkıp her seferide de döngüden çıkacağı için hep döngüde kalır ve çıkar 0-1-2 yi yazar sadece


# x = 0

# while x < 5:
#     x += 1 # Döngünün yukarıdaki sorunla karşılaşmaması için x + 1 in yukarıda yazılması gereklidir.
#     if x == 3:
#         continue
#     print(x)


# Örnek 1'den 100'e kadar tek sayıların toplamı

     
i = 0
result = 0

while i <= 100:
    i+= 1
    if i % 2 == 0 :
        continue
    result += i
print(result)
     