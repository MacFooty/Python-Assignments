addmore=1
dic={}
while (addmore):
	key=input('Key: ')
	value=input("Value: ")
	if(key not in dic):
		dic[key]=float(value)
	else:
		print("Key already exists in the dictionary.")
	addmore=int(input("Want to add more keys? (1/0) :"))

key=''
value=0
for i in dic:
	key+=i
	value+=dic[i]
print(str({key:value}))