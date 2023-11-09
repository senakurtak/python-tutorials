def count(values,query):
    count = 0
    for v in values:
        if v == query:
            count += 1
    return count

def deleteAll(values, query):
    c = count(values,query)
    for i in range(c):
        values.remove(query)
    return values

target = 5
my_list = [1,2,3,3,1,5,7,8,3,4,5]
print(my_list)
my_list = deleteAll(my_list, target)
print(my_list)