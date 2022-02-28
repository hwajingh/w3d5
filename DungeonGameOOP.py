import random

CELLS = [
(0,0),(1,0),(2,0),(3,0),(4,0),
(0,1),(1,1),(2,1),(3,1),(4,1),
(0,2),(1,2),(2,2),(3,2),(4,2),
(0,3),(1,3),(2,3),(3,3),(4,3),
(0,4),(1,4),(2,4),(3,4),(4,4),
]

def gameboard():
        ind = 0
        while ind <= 25:
            if ind < 5:
                for x in range(0,5):
                    print('[   ]', end="")
                    ind+=1
            elif ind < 10:
                print("\n")
                for x in range(5,10):
                    print(CELLS[x], end="")
                    ind+=1
            elif ind < 15:
                print("\n")
                for x in range(10,15):
                    print(CELLS[x], end="")                
                    ind+=1
            elif ind < 20:
                print("\n")
                for x in range(15,20):
                    print(CELLS[x], end="")
                    ind+=1
            elif ind < 25:
                print("\n")
                for x in range(20,25):
                    print(CELLS[x], end="")
                    ind+=1
            else:
                break
    
#subbing in whatever display method for CELLS[x] in print statement will work i.e. "  []  "
class Token ( ):
    #gameboard

    def __init__(self,playerPos, basketPos=5, monsterPos=3, eggcounter = 0, basketcounter = 0, doorPos = 0):
        self.playerPos = playerPos
        self.basketPos = basketPos
        self.monsterPos = monsterPos
        self.eggcounter = eggcounter
        self.basketcounter = basketcounter
        self.doorPos = doorPos

    def randomize(self):
        self.basketPos = (random.randint(0, 24))
        self.monsterPos = (random.randint(0, 24))
        self.egg1 = (random.randint(0, 24))
        self.egg2 = (random.randint(0, 24))
        self.egg3 = (random.randint(0, 24))
        self.playerPos = (random.randint(0, 24))

    def instructions(self):
        print ('\n')
        print('The Demogorgen has escaped the UpsideDown and is currently loose in Hawkins Middle School')
        print ('Your mission is to collect the basket, the eggs it has laid around your school, and then to run out the door')
        print ('Be careful the Demogorgon does not get you or you\'ll be dragged into the Upside-Down')

    def drawMap(self,playerPos):
        ind = 0
        while ind <= 25:
            if ind < 5:
                for x in range(0,5):
                    if self.playerPos == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            elif ind < 10:
                print("\n")
                for x in range(5,10):
                    if self.playerPos == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            elif ind < 15:
                print("\n")
                for x in range(10,15):
                    if self.playerPos == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")                
                    ind+=1
            elif ind < 20:
                print("\n")
                for x in range(15,20):
                    if self.playerPos == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            elif ind < 25:
                print("\n")
                for x in range(20,25):
                    if self.playerPos == x:
                        print("  P   ", end="")
                    else:
                        print(self.CELLS[x], end="")
                    ind+=1
            else:
                break
            return gameboard

    def movement(self):
        move = input("Do you want to move left/right/up/down or quit: \n")
        if move.lower() == "left":
            if self.playerPos % 5 ==0: #it is at left wall 
                print("you hit a wall, reselect a move")
            else:
                self.playerPos -=1 
                self.monsterPos +=1
                print(self.playerPos)
                print (self.monsterPos)
        elif move.lower() == "right":
            if self.playerPos != 4 and self.playerPos != 9 and self.playerPos != 14 and self.playerPos != 19 and self.playerPos != 24:
                self.playerPos +=1 
            else:
                print("you hit the wall, reselect a move")
        elif move.lower() == "up":
            if self.playerPos < 5:
                print("you hit a wall, reselect a move")
            else:
                self.playerPos-=5
                self.monsterPos -=3
                print(self.playerPos)
                print (self.monsterPos)
        elif move.lower() == "down":
            if (self.playerPos+5) >24:
                print("you hit a wall, reselect a move")
            else:
                self.playerPos+=5
                self.monsterPos +=2
                print(self.playerPos)
                print (self.monsterPos)
        elif move.lower() == "quit":
            #gameison = False
            print('trying to quit')
        else:
            print ('please enter a valid choice')
        return self.playerPos and self.monsterPos


    def eggs_on_board(self):
        self.eggset = {self.egg1,self.egg2,self.egg3}
        self.movement()
        if self.playerPos == self.egg1:
            if self.egg1 in self.eggset:
                print("you found egg 1")
                self.eggcounter+=1
                self.eggset.remove(self.egg1)
            elif self.egg2 not in self.eggset:
                print ('You already got an egg from here! Look somewhere else!')            
            print(f"so far you have found {self.eggcounter} of 3 eggs")
        elif self.playerPos == self.egg2:
            if self.egg2 in self.eggset:
                print("you found egg 2")
                self.eggcounter+=1
                self.eggset.remove(self.egg2)  
            elif self.egg2 not in self.eggset:
                print ('You already got an egg from here! Look somewhere else!')
            print(f"so far you have found {self.eggcounter} of 3 eggs")
        elif self.playerPos == self.egg3:
            if self.egg3 in self.eggset:
                print("you found egg3")
                self.eggcounter +=1
                self.eggset.remove(self.egg3)
            elif self.egg3 not in self.eggset:
                print ('You already got an egg from here! Look somewhere else!')
            print(f"so far you have found {self.eggcounter} of 3 eggs")
        else:
            print (self.eggcounter)
            print ('keep looking')

    def basket_on_board(self):
        self.movement()
        if self.playerPos == self.basketPos:
            self.basketcounter +=1
            print ("You've found your basket, now collect your eggs")
        else:
            print ('Keep looking for your basket!')

    def door_search(self):
        self.movement()
        if play_game.playerPos == play_game.doorPos:
            print ('You escaped the Demogorgen! Go celebrate with some waffles for Eleven')
        elif play_game.monsterPos == play_game.playerPos:
            print('The Demogorgen found you. Looks like you\'ll be stuck in the Upside Down')
        else:
            print ('Keep looking! You GOTTA GET OUTTA THERE')





gameboard()

play_game = Token(CELLS)
play_game.randomize()   
play_game.instructions()
# play_game.drawMap()


while play_game.basketcounter == 0:
    play_game.basket_on_board()
print ('now look for the eggs')

while play_game.eggcounter !=3:
    play_game.eggs_on_board()
print ('all eggs found')

print('Great! You\'ve found all the eggs for your basket!. Now RUNN to the door before Demogorgen gets you')
while play_game.playerPos !=play_game.doorPos:
    if play_game.monsterPos == play_game.playerPos:
        print('game over')
        break
    else:
        play_game.door_search()


while play_game.basketcounter == 1 and play_game.eggcounter == 3:
    play_game.door_search()
    break
    
#     #ending the game
# if play_game.basketcounter ==1 and play_game.eggcounter==3 and play_game.playerPos == play_game.doorPos:
#     print("You've successfully escaped the Demogorgon")
#     gameison = False
# elif play_game.playerPos == play_game.monsterPos:
#     print("You were captured by the Demogorgon!")
#     gameison = False

