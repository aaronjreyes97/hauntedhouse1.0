#import random and turtle
from random import*
import turtle

#map drawing
window = turtle.Screen()
window.bgcolor("black")
window.title("Haunted house map")
playerCursor = turtle.Turtle()
playerCursor.color("white")
playerCursor.speed(11)

playerCursor.pu()
playerCursor.left(90)
playerCursor.back(25)
playerCursor.right(90)
playerCursor.pd()

playerCursor.left(180)
playerCursor.forward(250)
playerCursor.right(90)
playerCursor.forward(50)
playerCursor.right(90)
playerCursor.forward(100)

for x in range(4):
    playerCursor.right(90)
    playerCursor.forward(50)
    playerCursor.backward(50)
    playerCursor.left(90)
    
    playerCursor.forward(100)

playerCursor.right(90)
playerCursor.forward(50)
playerCursor.right(90)
playerCursor.forward(250)
playerCursor.back(50)

playerCursor.left(90)
playerCursor.forward(50)
playerCursor.right(90)
playerCursor.forward(100)
playerCursor.right(90)
playerCursor.forward(200)

playerCursor.right(90)
playerCursor.forward(100)
playerCursor.right(90)
playerCursor.forward(100)
playerCursor.back(50)
playerCursor.right(90)
playerCursor.forward(300)
playerCursor.left(90)
playerCursor.forward(50)
playerCursor.left(90)
playerCursor.forward(100)
playerCursor.left(90)
playerCursor.forward(50)

playerCursor.pu()
playerCursor.goto(0, 0)
#end of map drawing

#Helper function reduces redundant code.         
def ghost_encounter_helper(playerStats, room):
    if (room == 1):
         mainHall(playerStats)
    elif (room == 2):
        #got to basement
        basement(playerStats)
    elif (room == 3):
        #go to dinning room
        diningRoom(playerStats)
    elif (room == 4):
        kitchen(playerStats)
        print()
    elif (room == 5):
        #go to living room
        livingRoom(playerStats)
    elif (room == 6):
        #go to ballroom
        ballroom(playerStats)
        print()
    elif (room == 7):
        #go to upstairs hall
        upstairsHallway(playerStats)
        print()
    elif (room == 8):
        #go to bedroom
        bedroom(playerStats)
        print()
    elif (room == 9):
        #go to bathroom
        bathroom(playerStats)
        print()
    elif (room == 10):
        #go to the attic
        attic(playerStats)
        print()
    elif (playerStats[1] <= 0):
        game_on = False
                
def ghost_encounter(playerStats, current_room):
    #lists of different ghosts and verbs were created to make variation!
    ghosts = ["tall shadowy man in a tattered business suit.",
     "a long, spindly man with a smile that stretches ear to ear.",
     "a pale woman in a white nightgown.",
        "a small girl with a pair of scissors. "]
    verbs = ["crawls ", "staggers ", "slowly floats ", "walks ", "flies "]
    print("A ghostly figure appears in front of you, it looks like " +str(ghosts[randint(0,3)]) +"The ghost " +str(verbs[randint(0,4)]) +"towards you with malice intent. What do you do?")
    while (playerStats[1] > 0):
        print("A) Run away! \nB) Fight! \nC) Use an item!")
        choice = input().upper()
        print()
        if (choice == "A"):
            print("* You turn tail and run away! The ghost gets a good swipe on you though. \n You lose 1 HP!")
            playerStats[1] = playerStats[1] - 1
            print("You run away for quite a while and appear in a random room.")
            #Picks random number and goes to that room. Fly you fools!
            rng_room = randint(1,10)
            
            #Rerolls so you don't run into the same room.
            while (rng_room == current_room):
                rng_room = randint(1,10)

            ghost_encounter_helper(playerStats, rng_room)
                
        elif (choice == "B"):
            print("* You put up your fists and give the ghost a good run for thier money, for a human at least.. \n You lose 2 HP")
            print()
            #reduce HP and then reduce ghost encounter chance.
            playerStats[1] = playerStats[1] - 2
            if (playerStats[1] <= 0):
                #This will be said if your character dies.
                print("Your injuries are too bad to continue. You decide to rest here. You don't wake up.")
                game_on = False
            else:
                break
            print()
            playerStats[4] = playerStats[4] - 5
            ghost_encounter_helper(playerStats, current_room)
            
        elif (choice == "C"):
            print("You have " + str(playerStats[6]) + " Snickers bar(s).")
            print("You have " + str(playerStats[7]) + " Anti-Ghost Spray(s).")
            print("You have " + str(playerStats[8]) + " Flashlight(s).")
            print("A) Snickers Bar \nB) Anti-Ghost Spray \nC) Flashlight \nWhat do you use?")
            choice = input().upper()
            if (choice == "A" and playerStats[6] > 0):
                print("You eat the snickers bar and feel restored! \n +2 HP")
                playerStats[6] -= 1
                playerStats[1] += 2
            elif (choice == "B" and playerStats[7] > 0):
                print("* You shoot the ghost with the spray. It screams a ghostly whail and fades away! \nYou have successfully repelled the ghost!")
                playerStats[7] -= 1
                ghost_encounter_helper(playerStats, current_room)
            else:
                print("* That won't help that much and you consider a different option.")
                continue
        else:
            print("* You second guess yourself and consider the options again.")
            continue
    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()
        
def mainHall(playerStats):
    print("You enter the main hall of the mansion. Some erie stairs extend to the upper floor,\n and a door seems to extend downward into a basement, there are doors to your left and right.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(0, 0)

    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 1)
    
    picking = True
    while (playerStats[1] >= 1):
        while picking:
            print("A) Go up the stairs")
            print("B) Go down through the door")
            print("C) Go through the door on the left")
            print("D) Go through the door on the right")
            print("E) Check yourself")
            print("F) Search the room")
            print("G) Check the door")
        
            choice = str(input("What do you want to do? "))

            if (choice == "a"):
                #go to upstairs hallway
                upstairsHallway(playerStats)
            elif (choice == "b"):
                #go to basement
                basement(playerStats)
            elif (choice == "c"):
                #go to living room
                livingRoom(playerStats)
            elif (choice == "d"):
                #go to dining room
                diningRoom(playerStats)
            elif (choice == "e"):
                #check yourself (before you wreck yourself)
                checkYourself(playerStats)
            elif (choice == "f"):
                #check room for items
                print("You check the room.")
                print("All you can see around you is old furniture and a broken chandelier. You are careful not to walk under the chandelier.")
            elif (choice == "g"):
                #check to see how good the door hint is
                #also checks for win condition
                if (playerStats[9] == 1):
                    print("You attempt to fit the key in the doorknob. It works! You're free!")
                    #win state
                    win_state()
                elif (playerStats[3] >= 2):
                    print("The door looks like it requires a key, it should be in the house somewhere")
            
                else:
                    print("The door is locked")
            else:
                print("You have to make a choice. The ghost has become more restless.")
                continue
                #chance for ghost encounter rate up?

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def basement(playerStats):
    print("You enter the basement. There's a foul stench you can't identify and the light flickers irregularly. You don't want to be here.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(0, -50)

    chance = randint(0,100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 2)

    picking = True
    while (playerStats[1] >= 1):
        while picking:
            print("A) Go to the Main Hall")
            print("B) Search the Room")
            print("C) Check yourself")

            choice = str(input("What do you want to do?"))
            if (choice == "a"):
                mainHall(playerStats)
            elif (choice == "b"):
                #if the user has the fuse item
                if (playerStats[5] == 1):
                    print("With the fuse placed carefully, you flip on the lights. You feel a pressure lifted as you make your way through the house. No reason to be afraid: you're out of the dark. Perhaps this place will be livable now.")
                    game_on = False
                    #win con!
                    win_state()
                else:
                #if the player doesn't have the fuse
                    print("You find nothing but a deeper sense of dread. You REALLY don't want to stay here any longer.")
                    choice = str(input("What do you want to do?"))
            elif (choice == "c"):
                checkYourself(playerStats)
                continue
            else:
                choice = str(input("What do you want to do?"))

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def livingRoom(playerStats):
    print("You enter the living room. The rustic furniture within the room is covered with a thin layer of dust, but you get the sense you aren't alone in this room.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(-100, 0)

    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 5)

    picking = True
    while (playerStats[1] >= 1):
        while picking:
            print("A) Go to the Main Hall")
            print("B) Go to the Ballroom")
            print("C) Search the room")
            print("D) Check yourself")

            choice = str(input("What do you want to do?"))
            if (choice == "a"):
                #go to main hall
                mainHall(playerStats)
            elif (choice == "b"):
                #go to the ballroom
                ballroom(playerStats)
            elif (choice == "c"):
                #check the room, find nothing
                print("A thorough search of the dusty room does nothing but disturb the furniture, agitate your sinuses, and leave you unsettled.")
                choice = str(input("What do you want to do?"))
            elif (choice == "d"):
                #check your stats
                checkYourself(playerStats)
            else:
                #to prevent invalid input
                choice = str(input("What do you want to do?"))

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def diningRoom(playerStats):
    print("You enter the dining room. Somehow relatively well lit in this dingy home, dirty plates covered in cobwebs still hold bones you hope are those of poultry.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(100, 0)

    chance = randint(0, 100)
    if (chance <=playerStats[4]):
        ghost_encounter(playerStats, 3)

    picking = True
    while (playerStats[1] >= 1):
        while picking:
            print("A) Go to the Main Hall")
            print("B) Go to the Kitchen")
            print("C) Search the room")
            print("D) Check yourself")

            choice = str(input("What do you want to do?"))

            if (choice == "a"):
                mainHall(playerStats)
            elif (choice == "b"):
                kitchen(playerStats)
            elif (choice == "c"):
                get = randint(1, 3)
                if playerStats[12] == 0:
                    playerStats[12] = 1
                    if (get == 1):
                        print("You found a Snickers bar! Despite the dankness of the house, it's pristine. You may need this")
                        playerStats[6] = (playerStats [6] + 1)
                        if(playerStats[8] >= 1):
                            print("Upon further inspection with your flashlight, you find a second! Hope you're hungry.")
                            playerStats[6] = (playerStats[6] + 1)
                    elif (get == 2):
                        print("You found a can of anti-ghost spray! What is this doing here? There's no telling if someeone else was here before you, but this is yours now. Hopefully you won't have to use it.")
                        playerStats[7] = (playerStats[7] + 1)
                        if(playerStats[8] >= 1):
                            print("There are actually two! Someone seemed to come in here prepared. Well, maybe on paper.")
                            playerStats[7] = (playerStats[7] + 1)
                    elif (get == 3):
                        print("You found a flashlight! The batteries still work. A good sign for your chances of getting out of here.")
                        playerStats[8] = (playerStats[8] + 1)
                        if(playerStats[8] >= 1):
                            print("Not only did you already have a flashlight beside the one you found, there's actually another one. One in each hand, and one in...your mouth maybe?")
                            playerStats[8] = (playerStats[8] + 1)
                else:
                    print("You find nothing here but dust.\n")
            elif (choice == "d"):
                checkYourself(playerStats)

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def kitchen(playerStats):
    
    print("You enter the kitchen, Leaving the Dining room behind you. The shelves are half full of a random assortment of foodstuffs.\nYou think you saw a bloody knife on the counter. There is a back door, but it's boarded up.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(200, 0)

    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 4)
    
    picking = True
    while (playerStats[1] >= 1):
        while picking:
            print("A) Go to the Dining Room")
            print("B) Check yourself")
            print("C) Search the room")
            print("D) Check the back door")
        
            choice = str(input("What do you want to do? "))

            if (choice == "a"):
                #go to dining room
                diningRoom(playerStats)
            elif (choice == "b"):
                #check yourself (before you wreck yourself)
                checkYourself(playerStats)
            elif (choice == "c"):
                #check room for items
                print("You check the room.")
                print("Remember that knife I mentioned when you walked in? Well, whatever it's covered in, it's definitely NOT covered in ketchup.")
            elif (choice == "d"):
                #check to see how good the door hint is
                #also check win state
                if (playerStats[2] >= 2 and playerStats[8] == 0):
                    print("The boards look like they could be pried off with a crowbar, perhaps there is one somewhere.")
                    if (playerStats[10] == 1):
                        print("The boards give way easily to your crowbar. The door behind them is unlocked. You can leave this accursed place!")
                        game_on = False
                        win_state()
                        #win state
                elif (playerStats[10] == 1):
                    print("The boards give way easily to your crowbar. The door behind them is unlocked. You can leave this accursed place!")
                    game_on = False
                    win_state()
                    #win state
                else:
                    print("The door is boarded up.")
            else:
                print("You have to make a choice. The ghost has become more restless.")

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def attic(playerStats):
    
    print("You enter the attic, most of what you can make out in the darkness is cobwebs and old furniture. There is no obvious means of escape from up here.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(0, 100)

    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 10)
    
    picking = True
    while (playerStats[1] >= 1):
        while picking:
            #presents options
            print("A) Go back down to the upstairs hallway")
            print("B) Check yourself")
            print("C) Search the room")
            print("D) Check the window\n")
            choice = str(input("What do you want to do? "))

            if (choice == "a"):
                #go to upstairs hallway
                upstairsHallway(playerStats)
            elif (choice == "b"):
                #check yourself (before you wreck yourself)
                checkYourself(playerStats)
            elif (choice == "c"):
                #makes sure you can't get multiple escape items from one room
                usedattic = 0
                #check room for items
                print("\nYou check the room.")
                randomItem = randint(1,3)
                if (playerStats[11] == 0):
                    playerStats[11] = 1
                    if (randomItem == 1):
                        if (playerStats[10] == 0):
                            print("\nYou found a crowbar. This might be useful.\n")
                            playerStats[10] = (playerStats[10] + 1)
                        else:
                            randomItem = randint(2,3)
                    elif (randomItem == 2):
                        if (playerStats[9] == 0):
                            print("\nYou found a key. This might be useful.\n")
                            playerStats[9] = (playerStats[9] + 1)
                        else:
                            randomItem = randint(1,3)
                    elif (randomItem == 3):
                        if (playerStats[5] == 0):
                            print("\nYou found a fuse. This might be useful.\n")
                            playerStats[5] = (playerStats[5] + 1)
                        else:
                            randomItem = randint(1,2)
                            continue
                else:
                    print("There's nothing here but dust.\n")
            elif (choice == "d"):
                print("\nYou look out the window, it's a long way down, you decide not to jump. That could hurt... like a lot.\n")
                continue
            else:
                print("\nYou have to make a choice. The ghost has become more restless.\n")
                continue

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()
    
def checkYourself(playerStats):
    print("\nName: " + playerStats[0])
    print("Health: " + str(playerStats[1]))
    print("Speed: " + str(playerStats[2]))
    print("Smarts: " + str(playerStats[3]))
    print("Snickers bars: " + str(playerStats[6]))
    print("Anti ghost spray: " + str(playerStats[7]) + "\n")
    if (playerStats[8] > 0):
        print("You have a Flashlight.")
    if (playerStats[10] == 1):
        print("You have a Crowbar.\n")
    elif (playerStats[9] == 1):
        print("You have a Key.\n")
    elif (playerStats[5] == 1):
        print("You have a Fuse.\n")
    else:
        print()

def ballroom(playerStats):
    print("The door slams closed behind you. The sound of a record scracthes to life as it plays 40's swing but off key and slower than usual.")
    print("The room is a giant ball room, at one time it was grandiose but now it lays in ruins.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(-200, 0)
    
    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 6)
        
    while (playerStats[1] > 0):
        print("What do you do?")
        print("A) Go back to the Living Room \nB) Check Yourself \nC) Interact \nD) Search Room")
        choice = input().upper()
        print()
        
        if (choice == "A"):
            livingRoom(playerStats)
            
        elif (choice == "B"):
            checkYourself(playerStats)
            print()
        elif (choice == "C"):
            print("You try to turn off the music but whenever you walk away from the device it resumes playing.")
            print()
        elif (choice == "D"):
            #check room for items
            print("\nYou check the room.")
            randomItem = randint(1,3)
            if (playerStats[11] == 0):
                playerStats[11] = 1
                if (randomItem == 1):
                    if (playerStats[10] == 0):
                        print("\nYou found a crowbar. This might be useful.\n")
                        playerStats[10] = (playerStats[10] + 1)
                    else:
                        randomItem = randint(2,3)
                elif (randomItem == 2):
                    if (playerStats[9] == 0):
                        print("\nYou found a key. This might be useful.\n")
                        playerStats[9] = (playerStats[9] + 1)
                    else:
                        randomItem = randint(1,3)
                elif (randomItem == 3):
                    if (playerStats[5] == 0):
                        print("\nYou found a fuse. This might be useful.\n")
                        playerStats[5] = playerStats[5] +1
                    else:
                        randomItem = randint(1,2)
                        continue
            else:
                print("You find nothing here but dust.\n")
                continue

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()
    
def bathroom(playerStats):
    print("You enter the bathroom. The tiles are cracked and the sound of dripping water can be heard from the sink.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(-200, 50)
    
    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 9)
        
    while (playerStats[1] > 0):
        print("What do you do?")
        print("A) Go back to the Bedroom \nB) Check Yourself \nC) Interact \nD) Search Room")
        choice = input().upper()
        print()
        
        if (choice == "A"):
            print("You leave the bathroom and return to the Bedroom")
            bedroom(playerStats)
        elif (choice == "B"):
            checkYourself(playerStats)
            print()
        elif (choice == "C"):
            print("* You look in the smashed mirror. Everything looks normal for a moment. Then your reflection smiles. You turn away from the mirror.")
            print()
        elif (choice == "D"):
            #check room for items
            print("\nYou check the room.")
            randomItem = randint(1,3)
            if (playerStats[11] == 0):
                playerStats[11] = 1
                if (randomItem == 1):
                    if (playerStats[10] == 0):
                        print("\nYou found a crowbar. This might be useful.\n")
                        playerStats[10] = (playerStats[10] + 1)
                    else:
                        randomItem = randint(2,3)
                elif (randomItem == 2):
                    if (playerStats[9] == 0):
                        print("\nYou found a key. This might be useful.\n")
                        playerStats[9] = (playerStats[9] + 1)
                    else:
                        randomItem = randint(1,3)
                elif (randomItem == 3):
                    if (playerStats[5] == 0):
                        print("\nYou found a fuse. This might be useful.\n")
                        playerStats[5] = playerStats[5] +1
                    else:
                        randomItem = randint(1,2)
                        continue
            else:
                print("You find nothing here but dust.\n")
        else:
            print("*You think about that, then decided to not do that.")

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def bedroom(playerStats):
    print("You see a large king sized bed that's covered in dust. Despite the age of the house, this room still looks comfortable.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(-100, 50)
    
    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 8)
        
    while (playerStats[1] > 0):
        print("What do you do?")
        print("A) Go to the Upstairs Hallway \nB) Go to the Bathroom \nC)Go to Check Yourself \nD) Interact \nE) Search Room")
        choice = input().upper()
        print()
        
        if (choice == "A"):
            print("You go into the Upstairs Hallway.")
            upstairsHallway(playerStats)
        elif (choice == "B"):
            print("You go into the Bathroom.")
            bathroom(playerStats)
        elif (choice == "C"):
            checkYourself(playerStats)
            print()
        elif (choice == "D"):
            print("You check out the bed, it's soft.")
            print()
        elif (choice == "E"):
            randomItem = randint(1,3)
            if playerStats[13] == 0:
                playerStats[13] = 1
                if (randomItem == 1):
                        if playerStats[8] == 0:
                            print("You found a snickers bar! Was it here for a midnight snack?")
                            playerStats[6] = (playerStats[6] + 1)
                        else:
                            print("Upon further inspection, there's another. Someone was hungry.")
                            playerStats[6] = (playerStats[6] + 2)
                elif (randomItem == 2):
                        if playerStats[8] == 0:
                            print("You found anti-ghost spray! They won't catch you lacking, even in your sleep.")
                            playerStats[7] = (playerStats[7] + 1)
                        else:
                            print("Upon further inspection, there's another. Ghost be gone.")
                            playerStats[7] = (playerStats[7] + 2)
                elif (randomItem == 3):
                        if playerStats[8] == 0:
                            print("You found a flashlight! Don't be afraid of the dark anymore.")
                            playerStats[9] = (playerStats[9] + 1)
                        else:
                            print("Upon further inspection, there's another. Let there belight!")
                            playerStats[9] = (playerStats[9] + 2)
            else:
                print("You find nothing here but dust.\n")
                continue
        else:
            print("*You think about that, then decided to not do that.")

    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def upstairsHallway(playerStats):
    print("The floor creeks softly under your weight. There are many doors in this hallway and the attic access ladder is down.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    playerCursor.goto(0, 50)
    
    chance = randint(0, 100)
    if (chance <= playerStats[4]):
        ghost_encounter(playerStats, 7)
        
    while (playerStats[1] > 0):
        print("What do you do?")
        print("A) Go to the Attic. \nB) Go to the Bedroom \nC) Go to the Main Hall. \nD) Check Yourself. \nE) Interact with the room. \nF) Search the Room.")
        choice = input().upper()
        print()
        
        if (choice == "A"):
            print("You climb the ladder to the Attic.")
            attic(playerStats)
        elif (choice == "B"):
            print("You take a door on your left, it's the master Bedroom.")
            bedroom(playerStats)
        elif (choice == "C"):
            print("You go back downstairs to the Main Hall")
            mainHall(playerStats)
        elif (choice == "D"):
            checkYourself(playerStats)
        elif (choice == "E"):
            print("There is a painting on the wall..the eyes look like they're following you.")
            print()
        elif (choice == "F"):
            print("You search the hallway but there's nothing useful.")
        else:
            print("*You think about that, then decided to not do that.")

    #This will be said if your character dies.
    else:
        print("Your injuries are too severe to continue. You decide to rest here. You don't wake up.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Game Over!")
        main_menu()

def win_state():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You've escaped! Congrats on winning!")
    main_menu()
    
def game_start():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #Name, health, speed, smarts, ghost encounter chance, fuse, snickers bar, anti ghost spray, flashlight, key, crowbar.
    playerStats = ["Player", 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    print("Employer: Aaah, you actually showed up? You're braver than most. People usually don't show up after the phone call.")
    print("Employer: So let's get things started. What is your name?")
    name = input()
    print()
    print("Employer: Really? That's your name?")
    print("Employer: Okay, now fill out this form. It'll tell me what you're good at")
    print()
    print("* You have 6 points, put them into health, speed, and smarts to your liking. The max for a stat is 3 and the min is 1")
    picking = True
    while picking:
        points = 6
        print(points," points left!")
        health = int(input("Health: "))
        print()
        if health > 3:
            print("Employer: No one is that tough. We're gona have to start a new form.")
            continue
        if health < 0:
            print("Employer: Are you made out of paper? Please be realistic and get a new form.")
            continue
        if health == 3:
            points -= 3
        elif health == 2:
            points -=2
        else:
            points -= 1
        print()

        print(points, " points left!")
        speed = int(input("Speed: "))
        print()
        if speed > 3:
            print("Employer: No one is that fast...We have to use a new form now.")
            continue
        if speed < 0:
            print("Employer: What are you, a snail? Grab a new form.")
            continue
        if points == 3 and speed == 3:
            print("Employer: Oh so you have no smarts at all? New form.")
            continue
        if speed == 3:
            points -= 3
        elif speed == 2:
            points -=2
        else:
            points -= 1
        print()

        print(points, " points left!")    
        smarts = int(input("Smarts: "))
        print()
        if smarts > 3:
            print("Employer: Who are you Albert Einstein? Be realistic and restart from the begining.")
            continue
        if smarts > 3:
            print("Employer: No one is that smart. Get a new form")
            continue
        if smarts < 0:
            print("Employer: Uh...I don't think you're that dumb...start over.")
            continue
        if smarts == 3:
            points -= 3
        elif smarts == 2:
            points -=2
        else:
            points -= 1
        print()

        if points > 0:
             print("Employer: You have left over points. Are you okay with this?")
             print("A) Yes!")
             print("B) Hold up a sec.. (Start over)")
             choice = input().upper()
             if choice == "A":
                 picking = False
             if choice == "B":
                 continue
             else:
                 print("Employer: I'm going to assume that was a no...Here, have a new form.")
                 continue
        else:
            print("Employer: Ah, not bad. Not bad at all. Are you okay with this form?")
            print("A) Yes!")
            print("B) Hold up a sec.. (Start over)")
            choice = input().upper()
            if choice == "A":
                picking = False
            if choice == "B":
                continue
            else:
                print("Employer: I'm going to assume that was a no...Here, have a new form.")
                continue
    playerStats[0] = name
    playerStats[1] = health
    playerStats[2] = speed
    playerStats[3] = smarts
    
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Employer: Alright, on your first mission you will be able to bring one item with you.")
    print("Employer: What would you like to bring?")
    print()
    print("A) Snickers Bar: A item that will restore some health.")
    print("B) Anti-Ghost Spray: It will make any ghost run away!")
    print("C) Flashlight: This will light the rooms you search. Maybe you'll find something more!")
    choosing = True
    while choosing:
        choice = input().upper()
        if choice == "A":
            playerStats[6] = 1
            choosing = False
        elif choice == "B":
            playerStats[7] = 1
            choosing = False
        elif choice == "C":
            playerStats[8] = 1
            choosing = False
        else:
            continue
    print("Employer: Alright! You're all set, now go to this address and see what you can do with those ghosts!")
    print("* The employer hands you a piece of paper with an address on it\n")

    mainHall(playerStats)

    #Temp to see if the variables are shown
    for x in playerStats:
        print(x)

def main_menu():
    #Prints the title 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("      Welcome to Huanted House CYA!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    #Asks them what they want to do
    game_on = True
    while game_on == True:
        print("a) Play")
        print("b) Instructions")
        print("c) Credits")
        print("d) Exit")
        choice = str(input()).upper()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        if choice == "A":
            game_start()
        elif choice == "B":
            print("Welcome to our game! \nChoose one of the options that are provided, explore the house and try to get out. Items will help you in your jounrney.")
            print()
        elif choice == "C":
            print("This game was created by Mike, Aaron, August, Atiqul, and Jay!")
            print()
        elif choice == "D":
            game_on = False
    else:
        print("Thanks for playing!")
        exit()

#Starts the game
main_menu()
