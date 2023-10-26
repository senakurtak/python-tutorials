summ = 0
count = 0

# sentinel değer
# eğer sayı -1 olursa

number = int(input("Enter a number:"))
'''
while number != -1:
    summ = summ + number # summ += number
    count = count + 1 # count += 1
    
    number = int(input("Enter a number: "))
    
print("Average:", summ/count)'''

# Sınavda sorulabilecek bir soru
while number != -1:
    if count > 2: # 0, 1, 2 durumlarında işlemi yapar, (3) olduğu durumda çıkışımızı verir
        print("You entered too many values")
        break
    if number<0:
        print("Negative values are not allowed")
        continue # başa dönmesini sağlar. İterasyona sebep olur
    #iterasyon -> döngünün kaç defa dönmesi
    summ = summ + number # summ += number
    count = count + 1 # count += 1
    number = int(input("Enter a number: "))
    
print("Average:", summ/count)