
empty_list = [] #creation

grades = [56, 43, 78, 2, 76, 14] #list with 3 elements

#indexing slicing

'''print(grades)
print(grades[2])
print(grades[-2])
print(grades[2:4]) # 0 1 2
print(grades[3:]) # 3 4 5
print(grades[::2]) # 0 2 4
print(grades[1:-1])'''

a = len(grades) # length of the list

weather = [22.1, 22.2, 22.3, 22.4, 22.5, 22.6, 22.7]

'''total = 0
for w in weather:
    total += w
    print(total, w)

average = total / len(weather)

print("Average: {:.2f} centigrad degrees". format(average)) 

total = 0
for i in range(7):
    total += weather[i]
    print("{} . Day: {:.2f} C".format(i+1, weather[i]))

average = total / len(weather)
print("Average: {:.2f} centigrad degreessss". format(average)) 
'''

total = 0
for i,w in enumerate(weather):
    print(i,w)