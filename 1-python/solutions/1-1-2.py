# Code Challenge 1-1-2
'''
Let' write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
'''
check_amount = float(input("Enter the amount of the restaurant check: $"))
tip_percent = float(input("Enter the tip percentage (e.g., 18 for 18%): "))
num_diners = int(input("Enter the number of diners: "))

<<<<<<< HEAD
amount = float(input("Enter the total check"))
tip = float(input("Enter the tip percent"))
diners = int(input("Enter number of diners: "))

# Calculate the total amount with tip.
tip_amount = amount * (tip / 100)
total_with_tip = amount + tip_amount

# Calculate what each person owes
amount_owed = total_with_tip / diners

# Output the results, formatted to two decimal places for currency.
print(f"Total camount: ${amount:.2f}")
print(f"Tip amount ({tip}%): ${tip_amount:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
print(f"Amount owed: ${amount_owed:.2f}")
=======
tip_amount = check_amount * (tip_percent / 100)
total_with_tip = check_amount + tip_amount
amount_per_diner = total_with_tip / num_diners

print(f"\nTotal amount with tip: ${total_with_tip:.2f}")
print(f"Each diner owes: ${amount_per_diner:.2f}")
>>>>>>> cdd60852901035171f503cea7a12809e83283a81
