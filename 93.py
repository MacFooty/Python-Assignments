string=list(input())
n=int(input())
string.remove(string[n-1])
ans=""
for i in string:
	ans+=i
print(ans)
