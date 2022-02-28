import random
CELLS = [
(0,0),(1,0),(2,0),(3,0),(4,0),
(0,1),(1,1),(2,1),(3,1),(4,1),
(0,2),(1,2),(2,2),(3,2),(4,2),
(0,3),(1,3),(2,3),(3,3),(4,3),
(0,4),(1,4),(2,4),(3,4),(4,4),
]

class Game:

    def __init__(self):
        pass

    #subbing in whatever display method for CELLS[x] in print statement will work i.e. "  []  "
    def drawMap(self,CELLS):
        ind = 0
        while ind <= 25:
            if ind < 5:
                for x in range(0,5):
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
    def __init__(self, playerPos, basketPos, monsterPos, ):
        self.playerPos = playerPos
        self.basketPos = basketPos
        self.monsterPos = monsterPos
        
    def counters(self,eggcounter,basketcounter,doorPos):
        self.eggcounter = 0
        self.basketcounter = 0
        self.doorPos = 0

class Egg (Token):
    def __init__(self,egg1,egg2,egg3):
        self.egg1 = egg1
        self.egg2 = egg2
        self.egg3 = egg3

    def randomize(self,egg1,egg2,egg3):
        # self.playerPos = (random.randint(0, 25))
        # self.basketPos = (random.randint(0, 25))
        # self.monsterPos = (random.randint(0, 25))
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




# while gameison = True:
#     drawMap()


#create function to print instructions
#create function to do count - basket, eggs, invisible from monster count    
# gameison = True
# while gameison:
initiate_game = Game()
initiate_game.drawMap(CELLS)
playerPos = (random.randint(0, 25))
basketPos = (random.randint(0, 25))
monsterPos = (random.randint(0, 25))
play_game = Token(playerPos, basketPos,monsterPos)
play_game.counters(0,0,0)
while play_game.basketcounter == 0 and play_game.eggcounter > 0:
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

    while play_game.basketcounter == 0:
        if play_game.playerPos == play_game.basketPos:
            play_game.basketcounter+=1
            print("you found a basket, now collect your eggs")
        break
    
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
    print("You've successfully escaped the Demogorgon")
    gameison = False
elif play_game.playerPos == play_game.monsterPos:
    print("You were captured by the Demogorgon!")
    gameison = False
    
    # ask for directions to move

else: 
    'find the door'