x=list(map(str,input().split()))
l=[]
for i in x:
	l.append(len(i))
print(max(l))