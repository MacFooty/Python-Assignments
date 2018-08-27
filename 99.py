x=list(input())
temp=[]
for i in range(len(x)):
	if(i%2==0):
		temp.append(x[i])
ans=''
for i in temp:
	ans+=i
print(ans)
