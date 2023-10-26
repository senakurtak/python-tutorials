#variables.py

'''
Integer (Tam sayilar) 4 19 567
Float - Double () 4.05 10000.50 -3456
String Metin tutariz "Metin" 'Metin'
'''

x = 5
y = 4.5
z = "Cihan"
z = 'Cihan'

q = 4 + 5

# = (eşittir bir atama operatörüdür)

w = x + y

print(w)

x = 6

print(w)

w = w + 3

print(w)



# type-> değişkenin tipini belirlemede kullanılır type(x)
# casting -> yeni bir tipe dönüştürme
print("find the types below")
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(q, type(q))
print(w, type(w))

print(4+5)
print(4-5)
print(4*5)
print(4/5)
print(4//5) #integer division
print(4**5) #power
print(43%5) #mod

print("-------")

# print("cihan" + 5)-> can only concaenate str not int to str

print("cihan"+"ak")
print("cihan""ak")
print("cihan"*2)

nick = "cihan" + "5"
nicko = "cihan" + str(5)
nickolas = "cihan" + str(x)
print("nick")
print(nick)
print(nicko)
print(nickolas)


# Kullanıcıdan gelen veri için de aynı atamalar yapılabilir

print(int("674") + 76)
print(float("4.32") + 3)
# print(int("cihan")) hata verir
a = str(int(str(int(str(3)))))
print(a, type(a))

x = float(x)
print(x, type(x))

print("-------")

x += 5 # x = x + 5
print(x)
x -= 5
print(x)
x /= 5
print(x)
x *= 5
print(x)


# Boolean Algebra

# Logic (Mantık) 0-1 Yanlış-Doğru False-True

# 5>4 -> True
print("a = 5 > 4")
a = 5 > 4
print(a, type(a))


print("a = 5 < 4")
a = 5 < 4
print(a, type(a))

a = 5 >= 4
print(a, type(a))

a = 5 == 4 # a = (5 == 4)
print(a, type(a))


a = 5 != 4 # a = (5 != 4)
print(a, type(a))


#not -> bir boolean değerinin tersini almaya yarar

a = False
b = True
print("------- Boolean Algebra")
print(not a)
print(a and b)
print(a or b)
