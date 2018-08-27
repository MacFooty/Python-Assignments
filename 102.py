x=input()
abc=set('abcdefghijklmnopqrstuvwxyz')
count=0
for i in x:
	if(i.lower() in abc and i.lower()==i):
		count+=1
print(count)