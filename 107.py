x=input()
abc=set('abcdefghijklmnopqrstuvwxyz')
num=set(['1','2','3','4','5','6','7','8','9','0'])
countabc=0
countnum=0
for i in x:
	if(i.lower() in abc):
		countabc+=1
	if(i in num):
		countnum+=1
print("Letters: ",countabc)
print("Digits: ",countnum)
