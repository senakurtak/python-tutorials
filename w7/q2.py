import random

stones = [] 

for i in range(6):
    x = random.randint(0,100)
    while x in stones:
        x = random.randint(0,100)
    stones.append(x)
    
if min(stones[::2])<min(stones[1::2]):
    print("Player 1 wins")
else:
    print("Player 2 wins")