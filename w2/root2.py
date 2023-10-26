# root.py      
# from math import sqrt
import math

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))


d = b**2 - 4 * a * c

# aşağıdaki her iki yapı da çalışır
'''
x1 = (-1 * b - sqrt(d)) / (2*a)
x2 = (-1 * b + sqrt(d)) / (2*a)
'''

# indentation fix -> shift tab

if d>0:
    x1 = (-1 * b - d**0.5) / (2*a)
    x2 = (-1 * b + d**0.5) / (2*a)
    
    print("First root:", x1)
    print("Second root:", x2)
elif d == 0:
    x = (-1 * b) / 2*a
    print("First root:", x)
    print("Second root:", x)
else:
    print("No real roots")