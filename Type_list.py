# Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
# What kind of unexpected input could you get?


x= ["Arya sloshed her beer, wondering", 15.27, "once upon a midnight dreary", "I will not madly deem that power", 10, "the sexton departed and I was left alone",254, 85, "by mdnight, the castle was silent and dark", 409, 713, "clearly, the prospect did not cheer them"]
y= []
sum=0
for count in range(len(x)):
    if isinstance(x[count],int):
    #ifinstance is a boolean. We are comparing all the elements in x to an integer
        sum=sum+(x[count])
        #sum, alerady defined as '0', now will be the values of x that are integers
    elif isinstance(x[count],float):
    #float is a number with decimals.
        sum=sum+(x[count])
        #sum will be all the decimal values in the list
    elif isinstance(x[count],str):
    #now, here comes the words!
        y.append(x[count]) 
        #list.append(x): Add an item to the end of the list; equivalent to a[len(a):] = [x].
if sum==0:
    print "This is a string type"
    print "String:", y 
    #to print the strings.
elif y==[]:
    print "This is an integer list"
    print "Sum:", sum
else:
    print "The list has mixed types"
    print "String:", y
    print "Sum:", sum



