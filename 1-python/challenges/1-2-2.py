# Challenge 1-2-2

# Write a program to accept numbers until the user enters: 0

# The program should count the number of positive and negative numbers entered, 
# and print those values after the 0 is entered. 

count = 0
positive_count = 0
negative_count = 0

while True:
    num = int(input("Enter a number (enter 0 to finish): "))
    
    if num == 0:
        break
    elif num > 0:
        positive_count = positive_count + 1
        count += 1
    else:  
        negative_count += 1
        count += 1
    
print(f"You entered {count} numbers in total.")
print(f"There are {positive_count} positive numbers.")
print(f"There are {negative_count} negative numbers.")