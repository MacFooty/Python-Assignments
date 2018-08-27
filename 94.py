str1=input()
str2=input()
assert(len(str1)==len(str2))
dict1={}
dict2={}
for i in range(len(str2)):
	if str1[i] not in dict1:
		dict1[str1[i]]=1
	else:
		dict1[str1[i]]+=1
	if str2[i] not in dict2:
		dict2[str2[i]]=1
	else:
		dict2[str2[i]]+=1
print(dict1==dict2)