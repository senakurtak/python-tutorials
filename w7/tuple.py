# tuple.py 

a = [3,5,5.5,"Sena",[1,3]]

# append -> eleman ekler
# if 5.5 in a: -> içinde 5.5 var mı?
# remove del -> eleman silme
# sort -> sıralama

b = (3, 5, "hakan")
# tuple değiştirilemez
# tuple a eleman eklenemez, çıkartılamaz

print(a)
print(b)
print(a[2])
print(b[1])


a = a + [67]
# b + b + 5 concatane
# print(b(1)) -> is not callable by this way
# b[1] = b[1] + 3 -> tuple değiştirilemez


client = []
client.append(("sena", 27, 75))
client.append(("büşra", 30, 100))
client.append(("sinan", 42, 45))
print(client)

for name, age, score in client:
    name, age, score = client

limit = 60
counter = 0
for c in client:
    name, age, score = c
    if score >= limit:
        counter += 1

print(counter, "clients has at least", limit, "score.")

name = input("Name:")
age = input("Age:")
score =int(age) + 10

client.append((name, age, score))
print(client)