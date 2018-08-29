n=int(input("Enter n: "))
def sieve(n):
    gen=(x for x in range(2,n+1))
    lis=[x for x in range(2,n+1)]
    ans=[]
    for i in gen:
        for j in lis:
            if(i!=j and j%i==0):
                ans.append(j)
    return set(lis)-set(ans)

print(sieve(n))
