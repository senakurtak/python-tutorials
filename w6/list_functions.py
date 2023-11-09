my_list = []
my_list.append(3)
my_list.append(5)
my_list.append(5)
my_list.append(5)
my_list.append(5)

my_list.index(5) # aranılan değerin hangi indexte olduğunu söyler, yoksa hata verir

my_list.insert(2, 92)
print(my_list)

my_list.remove(5) # ilk bulduğu elemanı listeden kaldırır
print(my_list)

for i in range(my_list.count(7)): # kaç tane 7 olduğunu bulur. Elemanları tek tek gezer 7 mi diye bakar ve sayar
    my_list.remove(7)

my_list.clear()

a = [2,4,6] + [1,3,5]
b = [7,8]
# a.append(b) # [2, 4, 6, 1, 3, 5, [7, 8]]
a.extend(b) # [2, 4, 6, 1, 3, 5, 7, 8]
print(a) 