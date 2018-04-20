'''
Assignment: Fun with Functions
Create a series of functions based on the below descriptions.
    Odd/Even: Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
    Multiply: Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
'''

#Odd/Even

def oddEven (start, end):
    for counter in range (start,end):
        print""
        if (counter%2)==0:
            #even number
            print "Number is", str(counter) + ". This is an even number"
        else:
            print "Number is", str(counter) + ". This is an odd number"
oddEven (1,2001)

'''Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
'''

def multiply (multList):
    for x in range (len(multList)):
        multList[x]*=5
    return multList
print (multiply([2, 4, 10, 16]))


'''
TODD's
def odd_even():
    for num in range(2001):
        if (num % 2 is 0):
            print "Number is {}. This is an even number".format(num)
        else:
            print "Number is {}. This is an odd number".format(num)

# odd_even()

def multiply(incoming_list):
    new_list = []
    for value in incoming_list:
        new_list.append(value*5)
    return new_list

the_list = [1,2,3,4,5,6]
# print multiply(the_list)

def multiply_with(incoming_list, factor):
    new_list = []
    for value in incoming_list:
        new_list.append(value*factor)
    return new_list

# print multiply_with(the_list, 10)


def layered_multiples(arr):
    new_array = []

    for value in arr:
        mini_array = []
        for times in range(value):
            mini_array.append(1)
        new_array.append(mini_array)

    return new_array

print layered_multiples(multiply_with([1,2,3],2))
'''




        

