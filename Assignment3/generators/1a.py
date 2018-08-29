n=int(input("Enter n: "))

def foo(n):
    lis=[x for x in range(2,n+1)]
    for i in lis:
        if(i!=''):
            for j in lis:
                if(j!=''):
                    if(i!=j and j%i==0):
                        lis[lis.index(j)]=''
        if(i!=''):
            yield i

for i in foo(n):
	print(i)