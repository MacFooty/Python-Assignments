from functools import reduce
a=list(map(float,input("Enter the list: ").split()))
avg=reduce(lambda x,y:x+y,a)/len(a)
print(avg)
