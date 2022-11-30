#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10/0 #darà errore => ZeroDivisionError: division by zero

# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#   x = 10/0 #==> qui scrivo il codice che potrebbe causare errori, se c'è errore, viene mandato al blocco di codice di exception
# except:
#   print("well that didn't work!")


# TODO: You can also catch specific exceptions

try:
  answer = input("what should i divide 10 by?")
  num = int(answer)  #casting della risposta in un int
  print (10/num)
except ZeroDivisionError as e:
  print("You can't divide by zero")
except ValueError as e:
  print("You didn't give me a valid number")
  print(e)
finally:#viene eseguito comunque anche se accade l'errore
  print("this code always runs")