str1=input()
str2=input()
count1=0
count2=0
for i in str1:
	count1+=1
for i in str2:
	count2+=1

if(count1>count2):
	print(str1)
elif(count2>count1):
	print(str2)
else:
	print("Both are of equal length.")