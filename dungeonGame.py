import random


playerPos = (random.randint(0, 25))
basketPos = (random.randint(0, 25))
monsterPos = (random.randint(0, 25))
egg1 = (random.randint(0, 25))
egg2 = (random.randint(0, 25))
egg3 = (random.randint(0, 25))

print(playerPos)
print(basketPos)
print(monsterPos)
print(egg2)
print(egg1)
print(egg3)

#check if anything is in the same positon
while egg1== egg2 or egg2== egg3 or egg3==egg1 or egg1==basketPos or egg2 == basketPos or egg3 == basketPos or monsterPos == basketPos or playerPos == monsterPos or playerPos == basketPos:
    playerPos = (random.randint(0, 25))
    basketPos = (random.randint(0, 25))
    monsterPos = (random.randint(0, 25))
    egg1 = (random.randint(0, 25))
    egg2 = (random.randint(0, 25))
    egg3 = (random.randint(0, 25))
    
    
    print(playerPos)
    print(basketPos)
    print(monsterPos)
    print(egg2)
    print(egg1)
    print(egg3)


CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),
  ]



def drawMap(posP):
    ind = 0
    while ind <= 25:
        if ind < 5:
            for x in range(0,5):
                if posP == x:
                    print("  P   ", end="")
                else:
                    print(CELLS[x], end="")
                ind+=1
        elif ind < 10:
            print("\n")
            for x in range(5,10):
                if posP == x:
                    print("  P   ", end="")
                else:
                    print(CELLS[x], end="")
                ind+=1
        elif ind < 15:
            print("\n")
            for x in range(10,15):
                if posP == x:
                    print("  P   ", end="")
                else:
                    print(CELLS[x], end="")                
                ind+=1
        elif ind < 20:
            print("\n")
            for x in range(15,20):
                if posP == x:
                    print("  P   ", end="")
                else:
                    print(CELLS[x], end="")
                ind+=1
        elif ind < 25:
            print("\n")
            for x in range(20,25):
                if posP == x:
                    print("  P   ", end="")
                else:
                    print(CELLS[x], end="")
                ind+=1
        else:
             break

gameison= True  
monsterPos = 27
print(f"you are playing the dungeon Game, your starting position is {CELLS[playerPos]}" )
eggcounter = 0
basketcounter =0
doorPos = 0
while(gameison):
    drawMap(playerPos)
    print("\n")
    print(f"so far you have found {eggcounter} eggs and {basketcounter} basket, door is at position 0,0")
    print("\n")
    move = input("left/right/up/down: \n")
    if move.lower() == "left":
        if playerPos % 5 ==0 or playerPos == 0: #it is at left wall 
            print("you hit the left wall reselect a move")
        else:
            playerPos -=1 
    elif move.lower() == "right":
        if playerPos != 4 and playerPos != 9 and playerPos != 14 and playerPos != 19 and playerPos != 24:
            playerPos +=1 
        else:
            print("you hit the right wall")
    elif move.lower() == "up":
        if playerPos < 5:
            print("you hit a upper wall")
        else:
            playerPos-=5
    elif move.lower() == "down":
        if (playerPos+5) >25:
            print("you hit a lower wall")
        else:
            playerPos+=5
    else:
        break
  
    if basketcounter == 0:
        if playerPos == basketPos:
            basketcounter+=1
            print("you found a basket, now collect your eggs")
    eggsac = [egg1, egg2, egg3]
    
    if eggcounter != 3: #if no basket no egg
        if basketcounter != 1 and playerPos in eggsac :
            print("you dont have a basket but here is an egg")
        else:
            if playerPos == egg1:
                    print("you found egg 1")
                    eggcounter+=1
            elif playerPos == egg2:
                    print("you found egg 2")
                    eggcounter+=1
            elif playerPos == egg3:
                    print("you found egg 3")
                    eggcounter+=1
            else:
                continue
    
    
    #ending the game
    if basketcounter ==1 and eggcounter==3 and playerPos == doorPos:
        print("you fininshed the game and escaped")
        gameison = False
    elif playerPos == monsterPos:
        print("you were eaten by the demogorgon!")
        gameison = False
    