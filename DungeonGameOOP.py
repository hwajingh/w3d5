import random
class Game:
    CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),
    ]

    def __init__(self,CELLS, posP):
        self.CELLS = CELLS 
        self.posP = posP

    #subbing in whatever display method for CELLS[x] in print statement will work i.e. "  []  "
    def drawMap(self):
        ind = 0
        while ind <= 25:
            if ind < 5:
                for x in range(0,5):
                    if self.posP == x:
                        print("  P   ", end="")
                    else:
                        print('[   ]', end="")
                    ind+=1
            elif ind < 10:
                print("\n")
                for x in range(5,10):
                    if self.posP == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            elif ind < 15:
                print("\n")
                for x in range(10,15):
                    if self.posP == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")                
                    ind+=1
            elif ind < 20:
                print("\n")
                for x in range(15,20):
                    if self.posP == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            elif ind < 25:
                print("\n")
                for x in range(20,25):
                    if self.posP == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            else:
                break
                

class Token (Game):
    def __init__(self, playerPos, basketPos, monsterPos, egg1, egg2, egg3):
        self.playerPos = playerPos
        self.basketPos = basketPos
        self.monsterPos = monsterPos
        self.egg1 = egg1
        self.egg2 = egg2
        self.egg3 = egg3
        self.eggcounter = 0
        self.basketcounter = 0
        self.doorPos = 0

    def randomize(self):
        self.playerPos = (random.randint(0, 25))
        self.basketPos = (random.randint(0, 25))
        self.monsterPos = (random.randint(0, 25))
        self.egg1 = (random.randint(0, 25))
        self.egg2 = (random.randint(0, 25))
        self.egg3 = (random.randint(0, 25))

    
        

#print(f'player: {self.playerPos} out of loop')
# print(f'basket:{basketPos} out of loop')
# print(f'monster:{monsterPos} out of loop')
# print(f'egg2:{egg2} out of loop')
# print(f'egg1:{egg1} out of loop')
# print(f'egg3: {egg3} out of loop')
# monsterPos = 25
#check if anything is in the same positon
# while egg1== egg2 or egg2== egg3 or egg3==egg1 or egg1==basketPos or egg2 == basketPos or egg3 == basketPos or monsterPos == basketPos or playerPos == monsterPos or playerPos == basketPos:
#     playerPos = (random.randint(0, 25))
#     basketPos = (random.randint(0, 25))
#     # monsterPos = (random.randint(0, 25))
#     egg1 = (random.randint(0, 25))
#     egg2 = (random.randint(0, 25))
#     egg3 = (random.randint(0, 25))
    
#print(f"you are playing the dungeon Game, your starting position is {CELLS[playerPos]}" )
#print (' Be careful of the Demogorgon - get too close and he can find you !')
#eggcounter = 0
#basketcounter =0
#doorPos = 0



# while gameison = True:
#     drawMap()


#create function to print instructions
#create function to do count - basket, eggs, invisible from monster count    
    

play_game = Token(1,15,2,3,4,5)
play_game.drawMap()
while play_game.basket_counter == 1 and play_game.eggcounter > 0:
    game_is_on = True
    print("\n")
    move = input("Do you want to move left/right/up/down or quit: \n")

    if move.lower() == "left":
        if play_game.playerPos % 5 ==0: #it is at left wall 
            print("you hit a wall reselect a move")
        else:
            play_game.playerPos -=1 
    elif move.lower() == "right":
        if play_game.playerPos != 4 and play_game.playerPos != 9 and play_game.playerPos != 14 and play_game.playerPos != 19 and play_game.playerPos != 24:
            play_game.playerPos +=1 
        else:
            print("you hit the wall")
    elif move.lower() == "up":
        if play_game.playerPos < 5:
            print("you hit a wall")
        else:
            play_game.playerPos-=5
    elif move.lower() == "down":
        if (play_game.playerPos+5) >25:
            print("you hit a wall")
        else:
            play_game.playerPos+=5
    elif move.lower() == "quit":
        break
    else:
        print ('please enter a valid choice')
  
    if play_game.basketcounter == 0:
        if play_game.playerPos == play_game.basketPos:
            play_game.basketcounter+=1
            print("you found a basket, now collect your eggs")
    
    if play_game.eggcounter != 3:
        if play_game.playerPos == play_game.egg1:
            if play_game.basketcounter == 1:
                print("you found egg 1")
                play_game.eggcounter+=1
            elif play_game.basketcounter == 0:
                print ('find the basket first to collect the eggs!')
            else:
                print ('somethings wonky1')
        elif play_game.playerPos == play_game.egg2:
            if play_game.basketcounter == 1:
                print("you found egg 2")
                play_game.eggcounter+=1
            elif play_game.basketcounter == 0:
                print ('find the basket first to collect the eggs!')
            else:
                print ('somethings wonky2')        
        elif play_game.playerPos == play_game.egg3:
            if play_game.basketcounter == 1:
                print("you found egg 3")
                play_game.eggcounter+=1
            elif play_game.basketcounter == 0:
                print ('find the basket first to collect the eggs!')
            else:
                print ('somethings wonky3')
        else:
            continue
    
    print("\n")
    print(f"so far you have found {play_game.eggcounter} eggs and {play_game.basketcounter} basket, door is at position 0,0")

    
    #ending the game
    if play_game.basketcounter ==1 and play_game.eggcounter==3 and play_game.playerPos == play_game.doorPos:
        print("You've successfully evaded the Demogorgon")
        gameison = False
    elif play_game.playerPos == play_game.monsterPos:
        print("you were eaten by the demogorgon!")
        gameison = False
    
            # ask for directions to move
else: 
    'find the door'