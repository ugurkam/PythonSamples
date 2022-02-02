message = 'Hello There. My name is ugur kam'
# message = message.upper() # bütün harfleri büyük harf yapar. 

# message = message.lower() # bütün harfleri küçük harf yapar.

# message = message.title() # Sadece baş harfleri büyük yapar.
# message = message.strip() # başta ve sondaki boşluğu alır.

# message = message.split() # her boşluktan cümleyi böler.
# message = message.split('.') # Noktalardan cümleyi böler.

# message = message.split()
# message = '-'.join(message) # parçalanmış cümleyi birleştirir. Parantez içindekini de aralara koyar.

#  index = message.find('name') # cümle içinde istediğim kelimeyi arayıp index sayısını geri döner

# isFound = message.startswith('H') # cümlenin tamamına bakıp hangi harf ile başlayıp başlamadığını teyit edebiliriz.
# isFound = message.endswith('m') # cümlenin tamamına bakıp hangi harf ile bitip bitmediğini teyit edebiliriz.

# message = message.replace('ugur', 'ufuk').replace('kam', 'demir') # cümlenin içinde kelime arayarak onları değiştirmeye yarar. Türkçe harfleri aratıp ingilizceye çevirebiliriz. 

# message =message.center(50, '*') # cümlenin tamamını verilen karakter sayısı içine ortalayarak yerleştirir ve isternirsa sağına ve soluna işaret konabiliriz.

message =message.center(50, '*')
print(message)