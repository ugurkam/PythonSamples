# 1- 'BMW, Opel, Mercedes,Mazda' elemanlarına sahip bir liste oluşturunuz.
# 2- liste kaç elemanlıdır?
# 3- Listenin ilk ve son elemanı nedir?
# 4- Mazda değerini toyota ile değiştirin.
# 5- Mercedes listenin bir elemanımıdır?
# 6- Listenin -2 indeksindeki değer nedir? 
# 7- Listenşn ilk 3 elemanını alın.
# 8- Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
# 10-Listenin son elemanını silin
# 11-Listenin elemanlarını tersten yazdırın.
# 12-Aşağıdaki verileri bir liste içinde saklayınız.

    # studentA: Yigit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan  1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

# 13-Liste elemanlarını ekrana yazıdırnın. 

# Cevaplar

# 1- 'BMW, Opel, Mercedes,Mazda' elemanlarına sahip bir liste oluşturunuz.

arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print(arabalar)

# 2- liste kaç elemanlıdır?

arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']
result = (len(arabalar))
print(result)

# 3- Listenin ilk ve son elemanı nedir?

arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']
result =arabalar[0]
print(result)
result =arabalar[-1]
print(result)


# 4- Mazda değerini toyota ile değiştirin.

arabalar[3] = 'Toyota'
result = arabalar
print(arabalar)

# 5- Mercedes listenin bir elemanımıdır?

result = 'Mercedes' in arabalar
print(result)

# 6- Listenin -2 indeksindeki değer nedir? 

result = arabalar[-2]
print(result)


# 7- Listenşn ilk 3 elemanını alın.

result = arabalar[0:3]
print(result)

# 8- Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.

# arabalar[3] = 'Renault'
# arabalar[2] = 'Toyota'

# print(arabalar)

# yada

arabalar[-2:] = ['Renault', 'Toyota']
print(arabalar)

# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.


# arabalar2= ['Audi', 'Nissan']
# arabalar3 = arabalar + arabalar2
# print(arabalar3)

# yada

result = arabalar + ['Audi', 'Nissan']
print(result)

# 10-Listenin son elemanını silin

# arabalar3.remove('Nissan') 

# yada

# arabalar.remove(arabalar[-1])

# print(arabalar)

# yada

del arabalar[-1]
result = arabalar
print(arabalar)

# 11-Listenin elemanlarını tersten yazdırın.

print(arabalar[::-1])

# 12-Aşağıdaki verileri bir liste içinde saklayınız

studentA = 'Yigit Bilgi 2010 (70,60,70)'
studentB = 'Sena Turan  1999 (80,80,70)'
studentC = 'Ahmet Turan 1998 (80,70,90)'

studentA = studentA.split()
studentB = studentB.split()
studentC = studentC.split()
students = studentA + studentB + studentC

print(students)

# 13-Liste elemanlarını ekrana yazıdırnın. 

students = studentA + studentB + studentC
print(students)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)