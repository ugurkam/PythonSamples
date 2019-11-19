def printshape(n):

    for i in range(0, n):
        print('*' * (n-i) + ' ' * (i*2) + '*' * (n-i))
    for j in range(1, n+1):
        print('*' * j + ' ' * (n-j)*2 + '*' * j)

printshape(int(input('input a number:')))