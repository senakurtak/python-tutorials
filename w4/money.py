'''
Yerel ve local değişikenler
'''

def pay(money,level):
    p = 3000 + level * 500
    money += p
    return money
a = "Sena"
money = 100
pay(money,3)
money = pay(money, 3)

print("My money is:", money)

