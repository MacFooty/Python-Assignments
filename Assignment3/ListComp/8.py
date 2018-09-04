x=list(map(float,input().split()))

x.sort()
ans=[]
for i in x:
	if(i not in ans):
		ans.append(i)
print(str(ans))