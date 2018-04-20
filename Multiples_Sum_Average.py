#Multiples
#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for count in range (1, 1000, 2):
    print (count) 

#Multiples
#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for count in range (5, 1000000, 5):
   print (count) 

#Sum List
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1, 2, 5, 10, 255, 3]))

#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    sum_numbers=sum_numbers/len(items)
    return sum_numbers
print(sum_list([1, 2, 5, 10, 255, 3]))
