x=list(map(int,input().split()))
odd=[]
even=[]
for i in x:
	if(i%2==0):
		even.append(i)
	else:
		odd.append(i)

print("Even: "+str(even))
print("Odd: "+ str(odd))