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
mtrav = 0
thr = 0
cTir = 0
nDis = -20
cDrk = 8
tTak = 0
while not done:
    oasis = random.randrange(0, 51)
    print(" ")
    print("A.Drink from your jelly bottle.")
    print("B.Run moderate speed.")
    print("C.Run full speed.")
    print("D.Stop for the night.")
    print("E.Status check.")
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
        print(" ")
    elif pIn.upper() == "D":
        print("You have traveled: ", mtrav, "miles!")
        cTir = 0
        print("Your caramel is greatful for the break! :)")
        print(" ")
        tTak += 1
        dAdd=random.randrange(12,16)
        nDis=nDis+dAdd
    elif pIn.upper() == "C":
        dAdd = random.randrange(10, 21)
        mtrav=mtrav+dAdd
        nDis -= dAdd
        thr+=1
        dAdd = random.randrange(2, 4)
        cTir+=dAdd
        dAdd = random.randrange(12, 16)
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
        dAdd = random.randrange(12, 16)
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
            print("Ahh, nice and refreshing!")
            print(" ")
        else:
            print("You're out of jelly :(")
            print(" ")


    if not done and thr>=4 and not cTir>=8 and not thr>=6 and not nDis>=0: #Thirst
        print("You're thirsty!")
        print(" ")
    elif thr>=6:
        time.sleep()
        print("You died of thirst :(")
        done = True
    elif not done and cTir>=4 and not cTir>=8 and not thr>=6 and not nDis>=0: #caramel
        print("Your caramel is getting tired")
        print(" ")
    elif cTir>=8:
        time.sleep(2)
        print("Your caramel is dead :(")
        print("You couldn't run away anymore and got caught")
        done = True
    elif not done and nDis>=-15 and not cTir>=8 and not thr>=6 and not nDis>=0: #witch
        print("The witch is getting close")
        print(" ")




    elif nDis>=0:
        print("The witch caught and ate you")
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
        print("Distance from witch: ", nDis)
        done = True


    elif oasis==5:
        print("YOU FOUND A JELLY BEAN FARM!")
        cTir=0
        thr=0
        cDrk=8







