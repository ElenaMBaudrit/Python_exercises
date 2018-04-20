"""
Find and Replace

In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
"""

words= "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day", "month")
print words #it will print the original string since the "replace" method returns a cpy of the string, not affecting the original one.


#Second exercise
#Min and Max
#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#Third exercise
#First and Last
#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
print len(x)
print x[0]
print x[len(x)-1]



#Fourth exercise
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
# split x into two lists.  
# what's the length? 11
# put the first 5 into a new list, the last 6 into another list
first_half = []
second_half = []
for index in range(11):
    if index < 5:
        first_half.append(x[index])
    else:
        second_half.append(x[index])

print first_half
print second_half
second_half.insert(0, first_half)
print second_half