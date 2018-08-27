x=input()
vow=['a','e','i','o','u']
count=0
for i in x:
	if(i.lower() in vow):
		count+=1
print(count)