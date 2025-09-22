## Challenge 1-4-2

##Let's make the code in 1-4-1 more resusable 

#re-write the date parse into a function `parsedate_mdy(text: str) -> datetime:`   
#re-write the date format into a function `formatdate_ymd(date: datetime) -> str:`  
#re-write the main program to use both functions. input -> parsedate -> formatdate -> output

import datetime
def parsedate_mdy(text: str) -> datetime.datetime:
    return datetime.datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d")

birthday = input("Enter your birthday: ")
date = parsedate_mdy(birthday)
formatted_date = formatdate_ymd(date)
print(formatted_date)
