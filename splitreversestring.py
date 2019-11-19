def reversestring(n):

    words = n.split()
    size = len(words)
            
    for index in range(size-1,-1,-1):
        print(words[index], sep='', end=' ')

reversestring(str(input('Bir yazi giriniz:')))