def delSpace(string):
	ans=''
	for i in string:
		if(i!=' '):
			ans+=1
	return ans

def countWords(string):
	count={}
	for i in string.split():
		if i.lower() not in count:
			count[i.lower()]=1
		else:
			count[i.lower()]+=1
	return count

def fileCount(file):
	f=open(file)
	a=f.read()
	f.close()
	return countWords(a)

def palindrome(string):
	a=list(string)
	b=a
	a.reverse
	return a==b

def sort(string):
	return string.split().sort()

def replace(string,key):
	ans=string.split()
	for i in range(len(ans)):
		if ans[i].lower()==key.lower():
			ans[i]=key
	return ans

def lowerAll(string):
	lis=string.split()
	ans=''
	for i in range(len(lis)):
		for j in lis[i]:
			ans+=j.lower()
	return ans

def upperAll(string):
	lis=string.split()
	ans=''
	for i in range(len(lis)):
		for j in lis[i]:
			ans+=j.upper()
	return ans

