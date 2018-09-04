z=[(i,j,k) for i in range(1,7) for j in range(1,7) for k in range(1,7)]
print(z)
dic={}
for i in z:
    for j in z:
        if(sorted(i)==sorted(j)):
            if(str(sorted(i)) not in dic):
                dic[str(sorted(i))]=1
            else:
                dic[str(sorted(i))]+=1

print("\n\n\n\n")
print(dic)