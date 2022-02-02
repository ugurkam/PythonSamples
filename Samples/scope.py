
# global scope

from mailbox import NoSuchMailboxError
from traceback import print_tb


x = 'global x'

def function():
    # local scope
    
    x = 'local x'

function()
print(x)


# Çıktısı:

# global x


# Fonksiyon içinde x tanımlandığında:

x = 'global x'
# global scope

def function():
    # local scope
    x = 'local x'
    print(x)

function()
print(x)

# Çıktısı:
    
# local x 
# global x



# Fonksiyon içinde x tanımlanmadığında:


x = 'global x'

def function():

    print(x)

function()
print(x)

# Çıktısı:
    
# global x
# global x


x = 'global x'
# global scope

def function():
    global x   # global x dediğimizde ise fonksiyon içindeki dışındakş x üzerinde değişiklik yapabilriiz.
    # local scope
    x = 'local x'
    print(x)

function()
print(x)

# Çıktısı:
    
# local x
# local x



###########################################

# global name
name = 'Cınar'

def changeName(newname):

# local name
    name = newname
    print(name)
    
changeName('ada')
print(name)

# Çıktısı:
    
# ada
# Cınar


# global name
name = 'Cınar'

def changeName(newname):
    global name
    name = newname
    print(name)
    
changeName('ada')
print(name)

# Çıktısı:
    
# ada
# ada



###########################################



name = 'global string'

def greeting():

    name = 'cinar'
    
    def hello():
        print('Hello ' + name)
        
    hello()

greeting()
print(name)

# Çıktısı:
    
# Hello cinar
# global string
    

#####################################

name = 'global string'

def greeting():

    name = 'cinar'
    
    def hello():
        name = 'ada'
        print('Hello ' + name)
        
    hello()

greeting()
print(name)

# Çıktısı:
    
# Hello ada
# global string




#####################################

name = 'global string'

def greeting():
       
    def hello():
        print('Hello ' + name)
        
    hello()

greeting()
print(name)

# Çıktısı:
    
# Hello global string
# global string



#####################################


x = 50

def test(x):

    print(f'x  {x} ')
    
    x = 100
    
    print(f'changed x to {x}')
    
test(x)
print(x)
    
# Çıktısı:
    
# x  50
# changed x to 100
# 50
    
    
x = 50

def test():
    global x
    print(f'x  {x} ')
    
    x = 100
    
    print(f'changed x to {x}')
    
test()
print(x)

# Çıktısı:
    
# x  50
# changed x to 100
# 100
