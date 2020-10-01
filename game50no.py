import random
x = random.randint(1, 50)
y = 0
print("play guessing game,only four chance there")
while(y < 4):
    z = int(input("guess between 1 to 50\n"))
    if z < x:
        print("lower than guess value")
    elif z > x:
        print("greater than guess value")
    elif z == x:
        print("congrates you guess right!!!")
        break
    y = y+1
if(y == 4):
    print("you loose all chance upppss!")
