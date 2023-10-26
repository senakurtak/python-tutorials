weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight/(height**2)

print("Your bmi:",bmi)
if bmi >= 20 and bmi <= 25:
    print("You are in good health")
else:
    print("You are in bad health")