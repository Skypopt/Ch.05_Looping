'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time
print("BISCUIT SKIDADDLE! (Cookie run rip off LOL)")
print("INSTRUCTIONS")
print("1. ESCAPE THE OVEN ON YOUR CARAMEL!")
print("2. Make sure to properly manage your thirst,")
print("and make sure your caramel isn't tired")
print("3. Don't get caught by the witch!!!")
done = False
foodBag=10
hung=0
wolfAcc=0
wolfDef=0
mtrav = 0
thr = 0
cTir = 0
nDis = -20
cDrk = 8
tTak = 0
#wolfAtk = random.randrange(0, 21)
while not done:
    wolfAtk = random.randrange(0, 21)
    oasis = random.randrange(0, 51)
    print(" ")
    print("A.Drink from your jelly bottle.")
    print("B.Run moderate speed.")
    print("C.Run full speed.")
    print("D.Stop for the night.")
    print("E.Status check.")
    print("F.Feed yourself")
    print("Q.Quit.")
    print(" ")
    pIn=str(input("What is your next choice?"))
    if pIn.upper() == "Q":
        print("Goodbye!")
        done = True
    elif pIn.upper() == "E":
        print("Miles traveled: ", mtrav)
        print("Drinks left: ", cDrk)
        print("Witches distance: ", nDis*-1)
        print("Caramel Tiredness: ", cTir)
        print("Thirst: ", thr)
        print("Hunger: ", hung)
        print("Food rations: ", foodBag)
        print(" ")
    elif pIn.upper() == "D":
        print("You have traveled: ", mtrav, "miles!")
        cTir = 0
        print("Your caramel is greatful for the break! :)")
        print(" ")
        tTak += 1
        dAdd=random.randrange(10,14)
        nDis=nDis+dAdd
    elif pIn.upper() == "C":
        dAdd = random.randrange(10, 21)
        mtrav=mtrav+dAdd
        nDis -= dAdd
        thr+=1
        dAdd = random.randrange(0, 4)
        hung+=dAdd
        dAdd = random.randrange(2, 4)
        cTir+=dAdd
        dAdd = random.randrange(7, 14)
        nDis+=dAdd
        tTak += 1
        print("FULL SPEED AHEAD!!!")
        print("You have traveled: ", mtrav, "miles!")
        print(" ")
    elif pIn.upper() == "B":
        dAdd = random.randrange(5, 12)
        mtrav+=dAdd
        nDis-=dAdd
        thr+=1
        cTir+=2
        dAdd = random.randrange(0,4)
        hung+=dAdd
        dAdd = random.randrange(7, 14)
        nDis+=dAdd
        tTak += 1
        print("Get moving!")
        print("You have traveled: ", mtrav, "miles!")
        print(" ")
    elif pIn.upper() == "A":
        tTak += 1
        if cDrk>0:
            thr=0
            cDrk-=1
            dAdd = random.randrange(1, 4)
            nDis = nDis + dAdd
            print("Ahh, nice and refreshing!")
            print(" ")
        else:
            print("You're out of jelly :(")
            print(" ")
    elif pIn.upper() == "F":
        tTak+=1
        if foodBag>0:
            hung=0
            foodBag-=1
            dAdd = random.randrange(2, 5)
            nDis = nDis + dAdd
            print("Yes some yummy food!")
            print(" ")
        else:
            print("You're out of food")
            print(" ")


    if not done and thr>=4: #and not cTir>=8 and not thr>=6 and not nDis>=0: #Thirst
        print("You're thirsty!")
        print(" ")
    elif thr>=6:
        time.sleep()
        print("You died of thirst :(")
        done = True
    if not done and cTir>=4: #and not cTir>=8 and not thr>=6 and not nDis>=0: #caramel
        print("Your caramel is getting tired")
        print(" ")
    elif cTir>=8:
        time.sleep(2)
        print("Your caramel is dead :(")
        print("You couldn't run away anymore and got caught")
        done = True
    if not done and nDis>=-15: #and not cTir>=8 and not thr>=6 and not nDis>=0: #witch
        print("The witch is getting close")
        print(" ")
    elif nDis>=0:
        print("The witch caught and ate you")
        done = True
    if not done and hung>=8: #and not cTir>=8 and not thr>=6 and not nDis>=0 and not nDis>=-15
        print("You're getting hungry")
        print(" ")
    elif hung>=10:
        print("You died of hunger")
        done = True

    if mtrav>=200:
        time.sleep(3)
        print("You won the game!")
        print("Here are your final stats")
        print("Turns taken: ", tTak)
        print("Caramel tiredness: ", cTir)
        print("Thirst: ", thr)
        print("Jelly left: ", cDrk)
        print("Miles traveled: ", mtrav)
        print("Distance from witch: ", nDis*-1)
        done = True


    if oasis==5:
        print("YOU FOUND A JELLY BEAN FARM!")
        cTir=0
        thr=0
        cDrk=8
    while wolfAtk==7 and not done:
    #if wolfAtk==7 and not done:
        print("You've been attacked by wolves during your travels")
        print("G: Defend yourself")
        print("H: Run")
        print("I: Accept fate")
        wolfResp = str(input("What will do you?: "))
        if wolfResp.upper()=="G":
            wolfDef = random.randrange(1,5)
            if wolfDef == 1:
                print("You failed to defend yourself and died :(")
                done = True
            elif wolfDef!=1:
                print("You fought the wolf off but lost half of your jelly")
                print(" ")
                cDrk=cDrk/2
                break
        elif wolfResp.upper()=="H":
            print("Silly goose, you're not faster than a wolf")
            done = True
        elif wolfResp.upper()=="I":
            wolfAcc = random.randrange(1,11)
            if wolfAcc == 1:
                print("The wolf ate you, could've fought back :(")
                done = True
            elif wolfAcc!=1:
                print("The wolf took pity on you and left")
                print(" ")
                break
            else:
                print("That is not an option")










