from math import*
a=int(input("enter the coefficient of x^2:"))
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant:"))
d=b**2-4*a*c
if d<0:
    real=-b/2*a
    img=sqrt(abs(d)) / 2*a
    root1=complex(real,img)
    root2=complex(real,-img)
else:
    root1 = (-b + sqrt(d)) / (2*a)
    root2 = (-b - sqrt(d)) / (2*a)

print("Root1:",root1," and Root2: ",root2)