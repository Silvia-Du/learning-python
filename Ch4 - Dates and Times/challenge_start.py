# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

#which day of the week do you want to count?
# 0: Monday etc
#Or 'exit' to quit

#loop chiedre domanda /opzioni/exit
#se exit esco da while
#raccolgo input GIORNO se non è exit contollo che sia un numero
# raccolgo input ANNO, controllo
# raccolgo input MESE, controllo

#creo un calendar 
def countdays(day, month, year):
  count = 0
  cal = calendar.monthcalendar(year, month)
  for week in cal:
    if week[day] != 0:
      count += 1
  return count


run = True
while(run):
  try:
    print("Which day of the week do you want to count?")
    print("0: Monday")
    print("1: Tuesday")
    print("2: Wednesday")
    print("3: Thursday")
    print("4: Friday")
    print("5: Saturday")
    print("6: Sunday")
    print("Or 'exit' to quit")
    day = input("?")
    if day.lower() == "exit":
      run = False
      break
    day = int(day)

    year = input("Insert Year: ")
    year = int(year)

    month = input("insert Month: ")
    month = int(month)

    result = countdays(day, month, year)
    print("-----------\n")
    print("There are "+ str(result) + "of those days in the month and year specified")
    print("-----------\n")

  except Exception as e:
    print(e)
    print("Sorry, that's not valid input")