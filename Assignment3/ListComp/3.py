from functools import reduce
a=list(map(float,input("Enter the list: ").split()))
maxz=reduce(lambda x,y: x if x>y else y,a)
minz=reduce(lambda x,y: x if x<y else y,a)
print("Max: ",maxz)
print("Min: ",minz)