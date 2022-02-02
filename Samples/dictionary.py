
# Key => Value olarak çalışır

# 34 => İstanbul
# 41 => Kocaeli

#sehirler = ['Kocaeli', 'İstanbul']
#plakalar = [41, 34]

#print(plakalar[sehirler.index('Kocaeli')])            # Burada Kocaeli ve İstanbulun indexleri bilindiği durumda



# Dictionary ile aşağıdaki kod ile istenilen value'ye ulaşılmalı.

# print(plakalar['Kocaeli']) => 41
# print(plakalar['İstanbul']) => 34

# Bunun içinde aşağıdaki şekilde tanımlama yapılmalı.

# plakalar = {'Key':'Value'}

plakalar = {'Kocaeli': 41, 'İstanbul':34}
print(plakalar['Kocaeli'])
print(plakalar['İstanbul'])

plakalar['izmir'] = 35 # İzmir key 35 value olarak plakalara eklenir.

print(plakalar)


users = {
    'ugurkam': {
        'age': 36,
        'roles': ['admin','user'], # dictionary içine liste konulabilir
        'email': 'ugurkam@gmail.com',
        'adres':'praha 7',
        'phone':'123456'},
    'burcakkam': {
        'age': 30,
        'roles': ['user'],
        'email':'bdk@gmail.com',
        'adres': 'Holesovice',
        'phone':'987654'}
}

print(users['ugurkam']['roles'][0]) # dictionary içindeki roles keyinin indexi ile istenen bilgiye ulaşılabilir. liste konulabilir
print(users['ugurkam'])