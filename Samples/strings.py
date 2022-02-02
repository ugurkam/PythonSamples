name = 'Ugur'
surname = 'Kam'
age = 36

greeting = ('my name is ' + name + ' ' + surname + ' and \nı am ' + str(age) + ' years old.')
length = len(greeting) # Greetingsin uzunluğunu bulur ve legthe atar
# print(greeting)
# print(len(greeting))

# print(greeting[0]) # Greetingsin 0 indexini getirir
# print(greeting[-1]) # Greetingsin -1 yani son indexini getirir
# print(greeting[3]) # Greetingsin 3 üncü indexine 4 üncü elemanınını getirir
# print(greeting[length-3]) # Greetingsin toplam index - 3 işlemindeki elamanını getirir
# print(greeting[3:7])  # Greetingsin 3 üncü indexten başlayıp 7 inci indexe kadar olan ( 7 dahil değil) elamanlarını getirir
# print(greeting[3:]) # Greetingsin 3 üncü indexten başlayıp devamındaki elemanların tamamını getirir
# print(greeting[:16]) # Greetingsin ilk  indexinden başlar 16 ıncı indexine (16 dahil değil) kadar olan elamanlarını getirir
print(greeting[2:40:3]) # Greetingsin 32 inci indexinden başlayarak 40 ınci indexine kadar 3 er atlayarak bulduğu elemanları getirir