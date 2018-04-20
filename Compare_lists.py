"""
Compare Lists
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:
"""
"""
cmp(): The method cmp() compares elements of two lists.
Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y.
https://www.tutorialspoint.com/python/list_cmp.htm
https://docs.python.org/2/library/functions.html#cmp
"""

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
cmp (list_one, list_two)
if list_one==list_two:
    print "This lists are the same."
else:
    print "The lists are not the same."

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
cmp (list_one, list_two)
if list_one==list_two:
    print "This lists are the same."
else:
    print "The lists are not the same."

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
cmp (list_one, list_two)
if list_one==list_two:
    print "This lists are the same."
else:
    print "The lists are not the same."

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
cmp (list_one, list_two)
if list_one==list_two:
    print "This lists are the same."
else:
    print "The lists are not the same."



'''
Tood's way

# Author Todd Enders Oct 2017

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if (list_one == list_two):
    print "The lists are the same"
else:
    print "The lists are not the same"

'''