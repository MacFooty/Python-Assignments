x=input()
abc=set('abcdefghijklmnopqrstuvwxyz')
up=0
down=0
for i in x:
	if(i.lower() in abc):
		up+=1
		if(i.lower()==i):
			down+=1

up=up-down
print("Uppercase: ",up)
print("Lowercase: ",down)
