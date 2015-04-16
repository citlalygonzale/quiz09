print ("Citlali Gonzalez")

import math
def distancia(a,b,c,d):
	g= c - a
	h= d - b
	g= g*g
	h= h*h
	i= g+h
	raiz= math.sqrt(i)
	return raiz

x1= int(input("Dame x1: "))
y1= int(input("Dame y1: "))
x2= int(input("Dame x2: "))
y2= int(input("Dame y2: "))
hipo= distancia(x1,y1,x2,y2)
print(hipo)
