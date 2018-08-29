n=int(input("Enter n: "))
def factor(n):
    i=2
    while(i<=int(n/2)+1):
        if(n%i==0):
            j=2
            count=0
            while(j<=int(i/2)+1):
                if(i%j==0):
                    count+=1
                    break
                j+=1
            if(count==0):
                yield(i)
        i+=1
        
for i in factor(n):
	print(i)