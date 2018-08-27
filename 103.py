x=input().lower()
y=list(x)
y.reverse()
ans=''
for i in y:
	ans+=i
print(ans==x)