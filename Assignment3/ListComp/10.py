import random as rnd

x=[[rnd.randint(1,6) for i in range(6)]for j in range(6)]
for i in range(6):
    print('---------------\n|', end=' ')
    for j in range(6):
        print(x[i][j],end=' ')
    print('|\n---------------')

