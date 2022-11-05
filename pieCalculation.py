import math
import random

print ('how many total trials do you want to try?')
totalTrials = input()
if "." in totalTrials:
    totalTrials == float
else:
    totalTrials == int
print ('what radius do you want your circle to be?')
radius = float(input())
withincount = 0
for trialnumbers in range(totalTrials):
    xcord = random.uniform(-1*radius, radius)
    ycord = random.uniform(-1*radius, radius)

    if math.sqrt(math.pow(xcord,2)+math.pow(ycord,2))<=radius:
        withincount = withincount + 1

        pi = ( 4* (withincount/totalTrials))

        print('Pi aproximation to your calculation is',pi)
