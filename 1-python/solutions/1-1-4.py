# Code Challenge 1-1-4¶
'''
Number to Letter grade
Letter grades in a college class are computed as follows:

95 and above is an A
75 and above, but below 95 is a B
50 and above, but below 75 is a C
below 50 is F
Write a program to input the number grade and calculate the letter grade

Re-write to account for "bad" grades > 120 or < 0
'''
try:
    grade = float(input("Enter the number grade: "))
    if grade > 100 or grade < 0:
        print("Error: Grade must be between 0 and 120.")
    elif grade >= 95:
        print("Letter grade is A")
    elif grade >= 75:
        print("Letter grade is B")
    elif grade >= 50:
        print("Letter grade is C")
    else:
        print("Letter grade is F") 
except ValueError:
    print("Invalid input. Please enter a numeric value for the grade.")