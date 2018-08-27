x=list(map(str,input().split()))
y=list(map(str,input().split()))
assert(len(x)==len(y))
dic={}

for i in range(len(x)):
	dic[x[i]]=y[i]
print(str(dic))
