'''
n = 5
Çıktı:
*
**
***
****
*****
'''
'''
sola yaslı yıldızlar
n = 6
for i in range(n): #    print('*' * i)
    for j in range(i+1): # yan yana yıldızlar
        print("*",end="")
    print("")
print("end")
'''

n = 6
for i in range(n): #    print('*' * i)
    for j in range(n-i-1): # yan yana yıldızlar
        print(" ", end="")
    for j in range(i+1):
        print("*",end="")
    print("")
print("end")