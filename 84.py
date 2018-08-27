x=list(map(str,input().split()))
word=input().lower()
n=int(input())
count=0
for i in x:
	if(i.lower()==word):
		count+=1
	if(count==n):
		x.remove(i)
		break
print((x))