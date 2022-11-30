#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def function1(): # : =>definisce l'inizio del contenuto della funzione come le {}
  print("i am a funcion") #l'indentazione deve esere identica per ogni riga

# TODO: function that takes arguments
def funct2(arg1, arg2):
  print(arg1, " ", arg2)


# TODO: function that returns a value
def cube(x):
  return x * x * x

# TODO: function with default value for an argument
def power( num, x=1 ):
  result = 1
  for i in range(x):
    result = result * num
  return result


# TODO: function with variable number of arguments

def multi_add(*args): #prenderà un numero indefinito di parametri :)
  result = 0
  for x in args:
    result = result + x
  return result

#se voglio parametri normali oltre ai multipli:
def multi_add2(arg1, *args):
  result = 0
  for x in args:
    result = result + x
  return result

#=>1

# function1() # esegue la funzione
# print(function1()) 

# # => questa ritorna due righe : i am a funcion e poi None => 
# # la prima è il risult dell'esecuzione della funz e il secondo è il tentativo di print di stampare la funz stessa

# print(function1) 

# qui la funzione non viene eseguita xke senza le parentesi => 
# viene stampato l'oggetto funzione che abbiamo creato : <function function1 at 0x0000020F8A7DA3B0>

#2 =>

# funct2(10, 20)
# print(funct2(10, 20))
# print(cube(3)) # se nn la metto in print non stampo in console xke ha solo il return e nn la stampa :)

#3 =>
# print(power(2)) 
# #il secondo argomento prende il valore di default della x
# print(power(2,3))
# print(power( x=3, num = 2))

#questi due hanno lo stesso risultato perchè con pyt posso cambiare l'oridne dei parametri purchè li chiami e valorizzi con il loro nome

#4 =>

print(multi_add(1, 2, 3))
