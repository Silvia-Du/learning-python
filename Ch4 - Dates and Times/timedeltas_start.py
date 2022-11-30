#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta # => è un ammount di time


# TODO: construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=1))


# # TODO: print today's date
now = datetime.now()
print("today is: ", now)

# # TODO: print today's date one year from now
print("one year from now il will be: ", str(now + timedelta(days=365))) # ==> (da che data, quanti gg togliere)

# # TODO: create a timedelta that uses more than one argument
print("in two weeks and 3 days it will be: ", str(now + timedelta(weeks=2 , days=3)))

# # TODO: calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks = 1)
s= t.strftime("%A %B %d, %Y")
print("one week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
  print("April fools Day already went by : ", ((today-afd).days))  #sto togliendo da today i gg in cui è statp April foolsday
  afd = afd.replace(year = today.year + 1)


# TODO: Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("It is", time_to_afd.days, "days until the next April fools' Day!")

