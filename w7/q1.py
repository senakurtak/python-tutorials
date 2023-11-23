def check(numbers, target):
    counter = 0
    for v in number:
        if v == target:
            counter+=1
        if counter == 2:
            return True
    return False
            
