addmore=1
dic={}
while (addmore):
	key=input('Key: ')
	value=input("Value: ")
	if(key not in dic):
		dic[key]=value
	else:
		print("Key already exists in the dictionary.")
	addmore=int(input("Want to add more keys? (1/0) :"))

query=input("Key to check: ")
print(query in dic)
