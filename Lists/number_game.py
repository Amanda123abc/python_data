import random 

# print(random.random())
# generates, random (floating point) # between 0-1 to certain decimal place

#print(random.uniform())
# requires set range from user (E.g. 1,10)

#print(random.unifrom(1,10))

#print(random.randint(1,10))
# random integer (whole number)
      
my_number = 13
com_number = random.randint(1,50)

while my_number != com_number:
    print(f"I chose the number: {com_number}")
    com_number = random.randint(1,50)

# Assignment 1 - week 4 

#? How long have i been alive?

import datetime

today_date = datetime.date.today()

dob = datetime.date(1989,6,4)

alive_for = today_date - dob

print(alive_for.days)



