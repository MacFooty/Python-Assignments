import random as rnd
z=[(round(rnd.random()*1000,4),rnd.randint(1,100)) for i in range(100)]	
z.sort(key=lambda x:x[0]*x[1])
print(z)