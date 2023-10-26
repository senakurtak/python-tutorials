# decision.py

# if - elif - else 

''' girintiler -> scope
if expression1:
    runs if expression1 is true
elif expression2:
    runs if expression2 is true
elif expresion3:
    run if expression3 is true
else:
    if all other expressions are false

'''

secret = 4
guess = int(input("Guess the number:"))

if guess<=10 and guess>=0:
    if guess < secret:
        print("Go up!")
    elif guess > secret:
        print("Go down!")
    else:
        print("Bingo!")
else:
    print("You entered an unvalid number!")
print("End!")