'''
Checkerboard
Write a program that prints a 'checkerboard' pattern to the console.
Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. 
In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping.
'''
for li in range (0,8):
    print""
    if (li%2)==0:
        #even li
        for ch in range (0,8):
            if(ch%2)==0:
                print'*',
            else:
                print ' ',
    else:
        #odd li
        for ch in range (0,8):
            if(ch%2)==0:
                print ' ',
            else:
                print '*',