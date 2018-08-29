n=int(input("Enter n: "))

def genRange(stop):
    count=0
    while count<stop:
        yield count
        count+=1

for i in genRange(n):
	print(i)