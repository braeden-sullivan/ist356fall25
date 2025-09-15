## Challenge 1-3-1

# Write a function called `average` which takes a list of numbers as input 
# then outputs the average of the numbers sum / count
# Call your function with an arbitrary list of numbers you create.

def average(nums):
    if not nums:
        return 0
    return sum(nums)/len(nums)

num_list = [10, 20, 30, 40, 50]
avg = average(num_list)
print(f"The average of {num_list} is {avg}")