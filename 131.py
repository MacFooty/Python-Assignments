x=input()
vow=set('aeiou')
count=0
for i in x:
	if(i.lower() in vow):
		count+=1
print(count)