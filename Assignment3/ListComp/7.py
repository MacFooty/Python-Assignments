x=list(map(float,input("Enter the list: ").split()))

leng=len(x)

def foo():
	least=min(x)
	x.remove(least)
	return least

y=[foo() for x in range(leng)]
print(y)
print(y[int(leng/2)] if leng%2==1 else (y[int(leng/2)]+y[int(leng/2)-1])/2)