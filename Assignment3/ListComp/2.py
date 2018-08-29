celsius=[x for x in range(-10,50,5)]
farenheit=list(map(lambda x:9/5*x+32,celsius))
print([(celsius[i],farenheit[i]) for i in range(len(celsius))])