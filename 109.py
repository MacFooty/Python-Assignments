x=input().split()
count={}
for i in x:
	if(i.lower() not in count):
		count[i.lower()]=1
	else:
		count[i.lower()]+=1
print(str(count))