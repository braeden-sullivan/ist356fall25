## Challenge 1-3-2

#Write a function called `cleanup` which takes a string as input and returns 
# a "cleaned string" meaning:
# - remove any ? , . or !
# - strip off the whitespace from the ends
# - return text in lower case
 
#write code to call your function and test it

def cleanup(input_string):
    cleaned_string = input_string.replace('?', '').replace(',', '').replace('.', '').replace('!', '')
    cleaned_string = cleaned_string.strip()
    cleaned_string = cleaned_string.lower()
    return cleaned_string

test_string = "  Hello, World! This is a test string.  "
cleaned = cleanup(test_string)
print(f"Original: '{test_string}'")
print(f"Cleaned: '{cleaned}'")
