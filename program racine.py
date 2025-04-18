import math
math.sqrt

print("Hello everybody! Today you are going to resolve a second degree equation.")
print("The equation that we're going to solve is : 4a²+5b-7")

a=input("What is the value of a ?")
b=input("What is the value of b ?")
c=7

a=float(a)
b=float(b)
c=float(c)

delta=b**2-4*a*c
delta=float(delta)

sqrt=b**2 

delta=(b**2)-4*a*c

if delta<0 :
  print("There are no roots.")

if delta>0 :
  x1=(-b+sqrt(delta))/(2*a)
  x2=(-b-sqrt(delta))/(2*a)
  print("there are 2 roots.")
