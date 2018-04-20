'''
Assignment: Stars
Write the following functions.
Part I
    Create a function called draw_stars() that takes a list of numbers and prints out *.
    For example:
        x = [4, 6, 1, 3, 5, 7, 25]
    draw_stars(x) should print the following when invoked:
        ****
        ******
        *
        ***
        *****
        *******
        *************************
'''
#PART I
'''
def draw_stars(x):
    for numbers in x:
        stars_str=""
        for y in range (numbers):
            stars_str+="*"
        print stars_str
draw_stars([4, 6, 1, 3, 5, 7, 25])

*******

Part II
    Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
    For example:
        x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    draw_stars(x) should print the following in the terminal:
        ****
        ttt
        *
        mmmmmmm
        *****
        *******
        jjjjjjjjjjj
'''
#The first function is the same as the previous one, only that an "if" was added to print the first character of each name.
def stars_letters(combined):
    for value in combined:
        if (type(value)is int): #type takes anything -- and I mean anything -- and returns its datatype. Integers, strings, lists, dictionaries, tuples, functions, classes, modules, even types are acceptable. 
                            #http://www.diveintopython.net/power_of_introspection/built_in_functions.html
            stars_str =""
            for x in range (value):
                stars_str +="*" #ALWAYS REMEMBER TO PUT THE +=  !!!!
            print stars_str
        else: #to print the first character of each name the same times as the amount of characters it has
            char_str="" #total of characters will be blank since it is a value that will change
            first_char= value[0].lower() #The letters must be in lower case.
            for times in range(len(value)):
                char_str += first_char
            print char_str 
stars_letters([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

