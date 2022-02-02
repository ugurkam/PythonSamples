numbers = [1, 10, 5, 16, 4, 9, 11]
letters = ['a','g','s','b','y','a','s',]

# val = numbers
# val = min(numbers) # minimumu val'e atar
# val = max(numbers) # maximumu val'e atar

# val = min(letters) # minimumu val'e atar alfabetik olarak ilk geleni
# val = max(letters) # maximumu val'e atar alfabetik olarak en sondaki

# val = numbers[3:6] # 3'den (3 dahil) 6'ıncı (6 dahil değil) indexe kadar olanları yaz
# val = numbers[0:3] # baştan (ilk karakter dahil) 3'üncü (3 dahil değil) indexe kadar olanları yaz

# val = numbers[4:] # 4'den (4 dahil) sonuncuya kadar (son dahil) olan karakterleri yaz


# numbers[4] = 40 # Numbersın 4. karakteri değiştiriyoruz 40 olarak.

# numbers.append(49) # Listenin en sonuna 49 elemanını ekler. 
# numbers.append(49)
# numbers.append(59)


# numbers.insert(3, 78) #  insert komutu ile 3. indexin önüne yeni karakteri ekledi. 3'e değil 3. önüne ekledi. (3. yü geçersen 3. olursun)

# numbers.insert(-1, 17) # En sondaki index numarasının önüne karakteri ekler

# numbers.insert(-2, 22) # En sondan ikinci index numarasının önüne karakteri ekler


# numbers.pop() # pop komutu ile en sondaki eleman silinir.

# numbers.pop(2) # parantez içine indeks numarasını denk gelen karakteri siler.

# numbers.remove(9) #  remove komutu ile parantez içindeki sayı bulunup silinir

# numbers.sort() # sort komutu ile liste küçükten büyüğe sıralanır

# letters.sort() # sort komutu ile liste alfabetik olarak üçükten büyüğe sıralanır


# numbers.reverse() # reverse komutu ile liste tersten yazdırılır. 
# letters.reverse() # reverse komutu ile liste tersten yazdırılır.


# print(numbers.count(10)) # count komutu ile numbers içerisinde kaç adet parantez içindeki sayıdan olduğunu saydırabiliriz.

numbers.clear() # clear komutu ile numbers içerisinde tüm elemanlar silinir ve boş bir dize gelir.
print(numbers)