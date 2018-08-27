x=input().split('-')
def out(word):
	return word.lower()
x.sort(key=out)
ans=''
for i in x:
	ans+=i+'-'
print(ans[:-1])