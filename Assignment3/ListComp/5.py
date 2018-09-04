x=list(map(float,input().split()))
import functools as f
import math
avg=f.reduce(lambda i,j:i+j,x)/len(x)

def diff(x):
	return (x-avg)**2
x=list(map(diff,x))
var=f.reduce(lambda i,j:i+j,x)/len(x)
sd=math.sqrt(var)
print("Average is: ",round(avg,3))
print("The variance is: ",round(var,3))
print("The standard deviation is: ",round(sd,3))