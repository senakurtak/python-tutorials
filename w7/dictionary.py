'''
list: "Kenan", "Sena", "Büşra", "Şeyma"
0 - "Kenan"
1 - "Sena"
2 - "Büşra"
3 - "Şeyma"
'''

'''
("cihan", 30, 75)
0 - name
1 - age
2 - score
'''

client1 = {"name":"cihan", "age":30, "score":100}

'''
dictionary - belli bir sıraya sahio olmaması için kullanıyoruz. Aslında python kendi implementasyonunda indexliyor
{"name":"cihan", "age":30, "score":100}
key -> value
'''
print(client1)
print(client1["name"])
client1["employed"] = True # employed diye bir key olmasa bile değişken oluşturur gibi oluşturup ekler
client1["age"] = 32
client1["cars"] = ['mercedes']
client1[1.1] = "2444"
client1[1.2] = "222444"
print(client1)
client1.pop(1.1) # pop ile 1.1 keywordüne sahip elemanı sildik
del client1[1.2] # del ile 1.2 e sahip elemanı sildik
print(client1)
for k in client1.keys():
    print(k)

print("----")
for v in client1.values():
    print(v)
    
for k,v in client1.items():
    print(k, "->", v) # eşlenen verileri değerlerini gösterir
    
for i in client1.items():
    print(i) #touple döndürür


if "job" in client1.keys():
    print(client1["job"]) # job diye değer varsa onu print
else:
    client1["job"] = "unemployed"
print(client1) # varsa jobu printler yoksa atama yapar