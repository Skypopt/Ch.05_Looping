  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = float(input("Enter a number: "))
    total+=x
print("The total is:", total)
  



  #2. print numbers from 2 to 100, inclusive.
for i in range(2,101):
    print(i)






'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=10
while i<=10 and i>=0:
    print(i)
    i=i-1
print("Blast off!")






'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
num=random.randrange(1,11)
print(num)







'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total2=0
posnum=0
negnum=0
zeronum=0
for i in range(7):
    num=float(input("Enter a number: "))
    if num <0:
        negnum+=1
    elif num >0:
        posnum+=1
    else:
        zeronum+=1
    total2+=num
print("Sum: ", total2)
print("Negatives: ", negnum)
print("Positives: ", posnum)
print("Zeros: ", zeronum)

