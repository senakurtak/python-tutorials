import random

def game():
    print("I think of a number, Guess what is it...")
    secret = random.randint(1, 100)
    guess = 0
    count = 0
    flag = False # did you loose from the count

    while guess != secret:
        print("secret is", secret)
        if count == 10:
            flag = True
            break
        guess = int(input("Guess:"))
        if guess<1 or guess>100:
            print("Please enter 1-100")
            continue
        if guess>secret:
            print("Down")
        elif secret>guess:
            print("Up")
        count += 1
    if flag:
        print("You lost!")
        return 0
    else:
        print("Bingo")
        return 1
    
    
end = False
score = 0
trial = 0

while not end:
    s = game()
    score += s
    trial += 1
    print("Scoreboard: ", score, "/", trial)
    ans = input("Would you like to play again?[Y/N]")
    if ans != "Y" and ans != "y":
        end = True
print("Thanks for playing!")