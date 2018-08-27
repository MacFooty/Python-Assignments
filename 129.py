x=input().split()
dic={}
for i in x:
	if(i[0].lower() not in dic):
		dic[i[0].lower()]=1
	else:
		dic[i[0].lower()]+=1
print(str(dic))