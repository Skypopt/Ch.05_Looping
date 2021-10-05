'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
q="n"
while q=="n":
    plyr = int(input("Chose rock, paper, or scissors! 1 for scissors, 2 for rock, 3 for paper"))
    if plyr == 1:
        print("Plyr: Scissors!")
    elif plyr == 2:
        print("Plyr: Rock!")
    elif plyr == 3:
        print("Plyr: Paper!")

    i=random.randrange(1,4)
    if i==1:
        print("Comp: Scissors!")
    elif i==2:
        print("Comp: Rock!")
    else:
        print("Comp: Paper!")

    if i==plyr:
        print("Tie game!")
    elif i==1 and plyr==2:
        print("You win!")
    elif i == 2 and plyr == 1:
        print("Computer wins!")
    elif i == 2 and plyr == 3:
        print("You win!")
    elif i == 3 and plyr == 2:
        print("Computer wins!")
    elif i == 3 and plyr == 1:
        print("You win!")
    elif i == 1 and plyr == 3:
        print("Computer wins!")

    q = str(input("Do you wish to quit?"))
    if q=="y":
        print("goodbye")
    else:
        print("Ok! Lets keep playing!")









