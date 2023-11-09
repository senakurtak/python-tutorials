def detectStar(values):
    for i in range(len(values)): # values list in uzunluğu kadar
        if values[i]>5:
            values[i] = 0
        print("In:", values)
    return values.count(0)

my_list = [3,4,5,6,7,8,9]

print(detectStar(my_list.copy())) # listenin kopyasını oluşturur
print(my_list)