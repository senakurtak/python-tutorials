# Create a function which input a list and check whether the sum of any two numbers equals a target number.

my_list = [0, 1, 2, 3, 4, 5]
target_Number = 3
def calculateChecker(values, target):
    for i in range(len(values)): 
        for j in range(i+1,len(values)):
            if values[i] + values[j] == target:
                print("Yes, {} plus {} equals {}".format(values[i], values[j], target))
            
            
calculateChecker(my_list, target_Number)