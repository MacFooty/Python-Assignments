x=list(map(int,input().split()))
sqrs=[]
digits=[]
import math
for i in range(x[0],x[1]+1):
	if(math.sqrt(i)==math.sqrt(i)//1):
		sqrs.append(i)
		count=0
		for j in str(i):
			count+=int(j)
		if(count<10):
			digits.append(j)
print(str(sqrs))
print(str(digits))