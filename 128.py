x=input().split()
dic={}
for i in x:
	if(i not in dic):
		dic[i]=1
	else:
		dic[i]+=1
print(str(dic))