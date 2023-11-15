
n = 100
for i in range(n): #    print('*' * i)
    for j in range(n-i-1): # yan yana yıldızlar
        print(" ", end="")
    for j in range(i+1):
        print("*",end="")
    print("")
print("trailing end")

for i in range(n):
    for j in range(i+1):
        print("*", end= "")
    print("")
print("leading end")

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1), end="")
    print(" " * (n - i - 1))
print("mid end")