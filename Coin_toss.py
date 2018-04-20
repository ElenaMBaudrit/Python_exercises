'''
Coin Tosses
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Sample output should be like the following:
    Starting the program...
    Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
    Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
    Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
    Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
    ...
    Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
    Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer
'''


import random
def coinToss ():
    head_count=0
    tails_count=0
    for counter in range(1,5001):
        x= random.randint(0, 1)
        if (x%2)==0:
            #heads
            head_count+=1
            print "Attempt #", counter, ": Throwing a coin... It's a head!... Got", head_count, " head(s) so far and ", tails_count, "tail(s) so far"
        else:
            #tails
            tails_count+=1
            print "Attempt #", counter, ": Throwing a coin... It's a tail!... Got", tails_count, " tails(s) so far and ", head_count, "head(s) so far"
coinToss()

'''
TODD's

import random

def cointosses():
    # flip a coin 5,000 times
    heads = 0
    tails = 0
    for toss in range(10):
        # how to determine head or tail
        # let's make a head 0 and a tail 1
        result = random.randint(0,1)
        # if we get a head or a 0, increment the head count
        if (result == 0):
            heads += 1
            output = "head"
        # if we get a tail, increment the tail count
        else:
            tails += 1
            output = "tail"
        
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(toss+1, output, heads, tails)

cointosses()
'''