'''
Object Oriented Programming
Nesne Tabanlı Programlama
Temel unsuru güvenlik; objeye ait özellik orada saklanırsa, başka entityler tarafından erişilemez.
'''
import random

import copy

class Human:
    
    # zorunlu değişkenler, zorunlu olmayanlardan önce gelmeli.
    def __init__(self, name, affiliation="N/A"):
        self.name = name
        # private oluşturmak için attributeların başında __ kullanırız -> __name 
        self.affiliation = affiliation
        self.money = random.randint(1000, 3000)
        self.bag = []
    
    def print(self):
        print("name: {}, company: {}, money: {}".format(self.name, self.affiliation, self.money))
    
    def buy(self, item, cost): # self -> sınıfa ait inputları kullanmak/nesnenin attributelarına erişmek için
        if cost <= self.money:
            self.money-=cost
            self.bag.append(item)
    
#hm = Human() #instance, human nesnesi
#print(hm.money)
#hm.buy("elma", 500)
#print(hm.money)

hm1 = Human("sena", "ITU")
hm2 = Human("busra", "YTU")
h3 = Human("merve")
hm4 = hm1 #objenin kendisi yok sadece kendisi var.

hm4.name = "mahmut" #aynı adresteki nesnenin ismini değişir, dolayısıyla hm1 ve hm4 name değişir.

hm5 = copy.copy(hm1)

# gerçekten kopyalamak için -> import copy .copy(nesne)
hm1.print()
hm2.print()
h3.print()

names = ["cihan", "hakan", "merve"]
humans = []
for name in names:
    temp = Human(name)
    humans.append(temp)