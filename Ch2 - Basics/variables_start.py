# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
#multipli
mydict = {"one" : 1, "two" : 2}
#dizionario

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[4])
print(mytuple[1])

# use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2])
#il finale nn è compreso, se metto 5, stampa fino al 4
# nomelista[da dove : fino a dove : con che step ]

# you can use slices to reverse a sequence ===> INVERTIRE UNA LISTA
print(mylist[::-1])
#così prenderà [default start: default end: a sep di -1] = lo stampa al contrario

# dictionaries are accessed via keys ===> accedo al valore delle chiavi negli oggetti
print(mydict["one"])

# ERROR: variables of different types cannot be combined
#se cerco di concatenare tipi diversi a python non piace

#print("ciaone"+ 123)

# avrò questo errore = TypeError: can only concatenate str (not "int") to str
#devo usare il casting con una funzione di python = str ===>
print("ciaone" + str(123))



# Global vs. local variables in functions
# creo una funz
def myFunction():
  #definisco una var interna uguale a una globale
  mystr = "nuova str"
  print(mystr)

myFunction()
print(mystr)
#nella funzione pyth crea una copia locale delle variabili dichiarate al suo interno 
# = mystr dentro è diversa da mystr dichiarata globalmente
#per crearla globalmente devo dire alla funzione che ne esiste una globale

def myFunction():
  global mystr
  #questo dice a pyt che esiste nel namespace questa var
  mystr = "nuova str"
  print(mystr)

myFunction()
print(mystr)

#eliminare una variabile 
del mystr
#print(mystr) # ==> darà problemi perchè con del la var nn esiste piu


