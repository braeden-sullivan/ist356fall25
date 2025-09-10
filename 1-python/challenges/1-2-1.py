# Challenge 1-2-1

## Write a program to accept a password as input. 
## If the password input is "secret" display "access granted"
## else say "invalid password"

## repeat the above up to 5 times. when the correct password is entered, stop looping
## when 5 loops have exhaused print "you are locked out"

attempts = 0
max_attempts = 5
while attempts < max_attempts:
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted")
        break
    else:
        attempts += 1
        print("Invalid password")

        if attempts == max_attempts:
            print("You are locked out")