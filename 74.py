x=list(map(int,input("Enter the list: ").split()))
ans=[]
for i in x:
	ans.append((i,i**2))

print(str(ans))