import random


# FIX: random.sample() gives six distinct positions in range(25) in one
# step. The original drew randint(0, 25) — 26 values for 25 cells, so a
# position of 25 would index past CELLS — and on any duplicate it re-rolled
# ALL six positions instead of just the colliding one.
playerPos, basketPos, monsterPos, egg1, egg2, egg3 = random.sample(range(25), 6)

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
    # FIX: one loop over 5 rows, instead of five copy-pasted row blocks.
    for row in range(5):
        for x in range(row * 5, row * 5 + 5):
            if posP == x:
                print("  P   ", end="")
            else:
                print(CELLS[x], end="")
        print()

gameison= True  

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
        if playerPos % 5 != 4:  # FIX: right wall is every 5th cell, not an enumerated list
            playerPos +=1 
        else:
            print("you hit the right wall")
    elif move.lower() == "up":
        if playerPos < 5:
            print("you hit a upper wall")
        else:
            playerPos-=5
    elif move.lower() == "down":
        if (playerPos+5) > 24:
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
