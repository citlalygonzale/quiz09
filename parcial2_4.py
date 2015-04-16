def fibonacci(m):
	a=1
	b=1
	c=a + b
	for i in range (m-1):
		a=b
		b=c
		c=a + b
	return a

m=int(input("Dame un entero positivo: "))
fb=fibonacci(m)
print("El fibonacci del numero",m,"= ",fb)
