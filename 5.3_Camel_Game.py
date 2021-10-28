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
camelFood = False
weaponry = False
foodBag=10
hung=0
wolfAcc=0
wolfDef=0
mtrav = 0
thr = 0
cTir = 0
nDis = 20
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
    print("G.Scavenge")
    print("Q.Quit.")
    print(" ")
    pIn=str(input("What is your next choice?"))
    if pIn.upper() == "Q":
        print("Goodbye!")
        done = True
    elif pIn.upper() == "E":
        print("Miles traveled: ", mtrav)
        print("Drinks left: ", cDrk)
        print("Witches distance: ", nDis)
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
        nDis=nDis-dAdd
    elif pIn.upper() == "C":
        if camelFood is False:
            dAdd = random.randrange(10, 21)
            mtrav=mtrav+dAdd
            nDis += dAdd
            thr+=1
            dAdd = random.randrange(0, 4)
            hung+=dAdd
            dAdd = random.randrange(2, 4)
            cTir+=dAdd
            dAdd = random.randrange(7, 14)
            nDis-=dAdd
            tTak += 1
            print("FULL SPEED AHEAD!!!")
            print("You have traveled: ", mtrav, "miles!")
            print(" ")
        elif camelFood is True:
            dAdd = random.randrange(20, 28)
            mtrav = mtrav + dAdd
            nDis += dAdd
            thr += 1
            dAdd = random.randrange(0, 4)
            hung += dAdd
            dAdd = random.randrange(2, 4)
            cTir += dAdd
            dAdd = random.randrange(7, 14)
            nDis -= dAdd
            tTak += 1
            print("FULL SPEED AHEAD!!!")
            print("Your special caramel feed gives your steed a boost")
            print("You have traveled: ", mtrav, "miles!")
            print(" ")
    elif pIn.upper() == "B":
        if camelFood is False:
            dAdd = random.randrange(5, 12)
            mtrav+=dAdd
            nDis+=dAdd
            thr+=1
            cTir+=2
            dAdd = random.randrange(0,4)
            hung+=dAdd
            dAdd = random.randrange(7, 14)
            nDis-=dAdd
            tTak += 1
            print("Get moving!")
            print("You have traveled: ", mtrav, "miles!")
            print(" ")
        elif camelFood is True:
            dAdd = random.randrange(10, 18)
            mtrav += dAdd
            nDis += dAdd
            thr += 1
            cTir += 2
            dAdd = random.randrange(0, 4)
            hung += dAdd
            dAdd = random.randrange(7, 14)
            nDis -= dAdd
            tTak += 1
            print("Get moving!")
            print("Your special caramel feed is giving your steed a boost")
            print("You have traveled: ", mtrav, "miles!")
            print(" ")
    elif pIn.upper() == "A":
        tTak += 1
        if cDrk>0:
            thr=0
            cDrk-=1
            dAdd = random.randrange(1, 4)
            nDis = nDis - dAdd
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
            nDis = nDis - dAdd
            print("Yes some yummy food!")
            print(" ")
        else:
            print("You're out of food")
            print(" ")
    elif pIn.upper() == "G":
        dAdd = random.randrange(1, 50)
        if dAdd==1 or dAdd==6 or dAdd==10 or dAdd==14 or dAdd==18 or dAdd==22 or dAdd==26 or dAdd==30 or dAdd==34 or dAdd==38 or dAdd==42 or dAdd==46:              #Add rest of numbers
            print("You found more food!")
            foodBag=10
        elif dAdd==2 or dAdd==7 or dAdd==11 or dAdd==15 or dAdd==19 or dAdd==23 or dAdd==27 or dAdd==31 or dAdd==35 or dAdd==39 or dAdd==43 or dAdd==47:
            print("You found a weapon")
            weaponry = True
        elif dAdd==3 or dAdd==8 or dAdd==12 or dAdd==16 or dAdd==20 or dAdd==24 or dAdd==28 or dAdd==32 or dAdd==36 or dAdd==40 or dAdd==44 or dAdd==48:
            print("You found water!")
            cDrk=8
        elif dAdd==4 or dAdd==9 or dAdd==13 or dAdd==17 or dAdd==21 or dAdd==25 or dAdd==29 or dAdd==33 or dAdd==37 or dAdd==41 or dAdd==45 or dAdd==49 or dAdd==50:
            print("You found nothing :(")
        elif dAdd==5:
            print("You found super caramel food!")
            camelFood = True
        dAdd = random.randrange(5, 15)
        nDis-=dAdd

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
    if not done and nDis<=15: #and not cTir>=8 and not thr>=6 and not nDis>=0: #witch
        print("The witch is getting close")
        print(" ")
    elif nDis<=0:
        print("The witch caught and ate you")
        done = True
    if not done and hung>=8: #and not cTir>=8 and not thr>=6 and not nDis>=0 and not nDis>=-15
        print("You're getting hungry")
        print(" ")
    elif hung>=10:
        print("You died of hunger")
        done = True

    if mtrav>=400:
        time.sleep(3)
        print("You won the game!")
        print("Here are your final stats")
        print("Turns taken: ", tTak)
        print("Caramel tiredness: ", cTir)
        print("Thirst: ", thr)
        print("Jelly left: ", cDrk)
        print("Miles traveled: ", mtrav)
        print("Distance from witch: ", nDis)
        done = True


    if oasis==5:
        print("YOU FOUND A JELLY BEAN FARM!")
        cTir=0
        thr=0
        cDrk=8
    while wolfAtk==7 and not done:
    #if wolfAtk==7 and not done:
        print("You've been attacked by wolves during your travels")
        print("H: Defend yourself")
        print("I: Run")
        print("J: Accept fate")
        wolfResp = str(input("What will do you?: "))
        if wolfResp.upper()=="H":
            if weaponry is True:
                wolfDef = random.randrange(1, 15)
                if wolfDef == 1:
                    print("You failed to defend yourself and died :(")
                    done = True
                elif wolfDef!=1:
                    print("You fought the wolf off but lost half of your jelly")
                    print(" ")
                    cDrk=cDrk/2
                    break
            else:
                wolfDef = random.randrange(1, 5)
                if wolfDef == 1:
                    print("You failed to defend yourself and died :(")
                    done = True
                elif wolfDef != 1:
                    print("You fought the wolf off but lost half of your jelly")
                    print(" ")
                    cDrk = cDrk / 2
                    break


        elif wolfResp.upper()=="I":
            print("Silly goose, you're not faster than a wolf")
            done = True
        elif wolfResp.upper()=="J":
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











