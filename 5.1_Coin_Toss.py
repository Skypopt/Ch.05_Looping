'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random
t=0
h=0
for i in range(50):
    i=random.randrange(0,2)
    if i == 0:
        print("heads")
        h+=1
    elif i == 1:
        print("tails")
        t+=1
print("Heads: ", h)
print("Tails: ", t)




