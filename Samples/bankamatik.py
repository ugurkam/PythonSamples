from operator import truediv


UgurHesap = {
    'ad': 'Ugur Kam',
    'hesapNo': '123456',
    'bakiye': 4000,
    'ekHesap': 1000
}

BurcakHesap = {
    'ad': 'Burcak Kam',
    'hesapNo': '987654',
    'bakiye': 3000,
    'ekHesap': 2000
}



def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    
    ekhesap = ''
    toplambakiye = 0
    
    if miktar <= 0:
        print("0 TL yada '-' miktar girdiniz tutarı kontrol ediniz.")

    elif (hesap['bakiye']) >= miktar:
        hesap['bakiye'] -= miktar
        print(f"Paranızı alabilirsiniz. Bakiyeniz {hesap['bakiye']}")
    
    elif (hesap['bakiye']) <= miktar:
        if (hesap['bakiye'] + hesap['ekHesap']) >= miktar:
            print(f"Bakiyeniz {hesap['bakiye']} ek hesap bakiyeniz {hesap['ekHesap']}")
            
            ekhesap = (input('Ek hesap kullanılsın mı (E/H) '))
        
            if ekhesap == 'E':
                toplambakiye = (hesap['bakiye'] + hesap['ekHesap'])
                toplambakiye -= miktar
                print(f"Paranızı alabilirsiniz. Bakiyeniz {toplambakiye}")
                
            else:
                print(f"Ek hesap kullanılmamıştır. Bakiyenizi arttırınız Bakiyeniz {hesap['bakiye']}")
                       
          
        else:
            print('Bakiye yetersiz')
    
    
        
paraCek(UgurHesap, 5000)
paraCek(UgurHesap, 2000)

    