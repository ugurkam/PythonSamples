# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

# def repeatWord(word, repeat):
 
#     for i in range(repeat):
#         print(word)


# repeatWord('ali',2)

# Çıktısı:

# ali
# ali
   
# YADA BOYLE DE YAZILABİLİR:
    
# def repeatWord(word, repeat):
#     print(word * repeat)

# repeatWord('ali\n',2)

# Çıktısı:

# ali
# ali


# 2- Kendisine gönderilen sınırsız sayıdaki bir parametreyi bir listeye çeviren fonksiyonu yazınız.

# def changeToList(*params):
#     liste = []

#     for i in params:
#         liste.append(i)
    
#     return liste       
   
# result = changeToList(1,2,3,4,5,6,7,8,9,10,11,'fidan', 12,'ali',13,'ugur', 14,'ufuk', 15)

# print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon yapınız.

def isAsal(num1, num2):

    asalNumbers = []

    for i in range(num1, num2+1):
        if i > 1:
            for x in (range(2, i)):
                if i % x == 0:
                    break
            else:
                asalNumbers.append(i)     
    
    return asalNumbers

result = isAsal(1,10)

print(result)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şekline döndürünüz

# def tambolen(num1):
    
#     liste = []
    
#     for i in range(1,num1):
#         if num1 % i == 0:
#             liste.append(i)
    
#     return(liste)


# result = tambolen(20)

# print(result)