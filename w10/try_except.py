a = input("Enter a value: ")

b = 6


c = 0

try: # bunu yapmayı dene
    c = a + b
except: # hata durumunda excepte girerse de program akmaya devam eder.
    print("An error occured")


print(c)

