r=tuple(map(int,input().split()))
perfect=[]
ans=[]
for i in range(r[0],r[1]+1):
    if(math.sqrt(i)==math.sqrt(i)//1):
        perfect.append(i)  
for i in perfect:
    temp=str(i)
    count=0
    for j in temp:
        count+=int(j)
    if(count<10):
        ans.append(i)

print(str(perfect))
print(str(ans))