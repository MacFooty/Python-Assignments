x=input()
ans=''
for i in x:
	char=i
	if(i==' '):
		char='-'
	ans+=char
print(ans)