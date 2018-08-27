addmore=1
dic={}
while (addmore):
	key=input('Key: ')
	value=input("Value: ")
	if(key not in dic):
		dic[key]=value
	addmore=int(input("Want to add more keys? (1/0) :"))
print(dic)