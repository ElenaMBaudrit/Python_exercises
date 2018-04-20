"""
Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
"""

word_list=["sets", "queues", "questions", "technical", "as", "how", "the", "asked", "short"]
char="o"
#what we are looking for
found=[]
#whatever we might find
for index in word_list:
    if index.find(char)!=-1:
    #since the char is "o", whatever has the character will be different to -1, therefore, it will be in "found"
        found.append(index)
        #whatever meets the previous parameter, will be in the "found" new list.
print found
