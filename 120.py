addmore=1
dic={}
while (addmore):
	print("Dictionary 1")
	key=input('Key: ')
	value=input("Value: ")
	if(key not in dic):
		dic[key]=value
	addmore=int(input("Want to add more keys? (1/0) :"))

addmore2=1
dic2={}
while (addmore2):
	print("Dictionary 2")
	key2=input('Key: ')
	value2=input("Value: ")
	if(key2 not in dic2):
		dic2[key2]=value2
	addmore2=int(input("Want to add more keys? (1/0) :"))

for i in dic2:
	if(i not in dic):
		dic[i]=dic2[i]
print(str(dic))