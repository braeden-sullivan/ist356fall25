## Challenge 1-4-3

#Let's make the code in 1-4-2 more resusable!!! 

#move your functions into a module names `dateutils.py`

#import your functions from `dateutils.py` into `1-4-3.py`


from dateutils import parsedate_mdy, formatdate_ymd
birthday = input("Enter your birthday: ")
date = parsedate_mdy(birthday)
formatted_date = formatdate_ymd(date)
print(formatted_date)