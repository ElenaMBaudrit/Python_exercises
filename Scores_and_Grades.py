'''
Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
    Score: 60 - 69; Grade - D
    Score: 70 - 79; Grade - C
    Score: 80 - 89; Grade - B
    Score: 90 - 100; Grade - A
'''
'''
randint()
    Randint accepts two parameters: a lowest and a highest number.
    Generate integers between 1,5. The first value should be less than the second.
        import random
        print random.randint(0, 5)
'''
import random
def scoresGrades ():
    for x in range(10):
        counter= random.randint(60,102)
        if (counter <= 69):
            print "Score:", str(counter) +": Grade - D"
        elif (counter <=79):
            print "Score:", str(counter) +": Grade - C"
        elif (counter <=89):
            print "Score:", str(counter) +": Grade - B"
        elif (counter <=100):
            print "Score:", str(counter) +": Grade - A"
        elif (counter>100):
            print "End of program. Bye!"
scoresGrades ()

'''
TODD's

import random

def scores():
    print "Scores and Grades"
    for num in range(10):
        score = random.randint(60,100)
        if score >= 60 and score < 70:
            grade = "D"
        elif score < 80:
            grade = "C"
        elif score < 90:
            grade = "B"
        else:
            grade = "A"
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

scores()
'''
