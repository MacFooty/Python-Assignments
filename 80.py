tup=[(1,2),(2,3),(2,4),(9,0)]

def foo(tup):
	return tup[1]

tup.sort(key=foo)
print(str(tup))