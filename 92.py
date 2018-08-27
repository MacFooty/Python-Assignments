string=input()
y=list(string)
for i in range(len(y)):
	if(y[i]=='a'):
		y[i]='$'
ans=""
for i in y:
	ans+=i
print(ans)