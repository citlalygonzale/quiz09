

print ("Citlali Gonzalez")

def superpower(a,b):
	m=0
	for m in range(b):
		m= m+1
		s= pow(a,m)
	return s
a = int(input("Give me the number: "))
b = int(input("Give me the power: "))
sp = superpower(a,b)
print(sp)
