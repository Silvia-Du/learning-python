#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

#dichiaro una classe==> parola chiave: class , nome maiuscolo
class Vehicle(): 
  #costruttore
  def __init__(self, bodystyle): #init è la funzione che viene chiamata da phyton quando un'oggetto viene inizializzato
    #self è la referenza all'oggetto stesso
    self.bodystyle = bodystyle
    #creo una function
  def drive(self, speed):
    #definisco le sue property:
    self.mode = "driving"
    self.speed = speed

# EREDITARIETA' : creiamo una classe che estenda la prima ==>vehicle è una superclasse
class Car(Vehicle):
  def __init__(self, enginetype):   #creo il costruttore
    super().__init__("Car") #prende la base dal costruttore della superclasse
    #definisco altri paramentri
    self.wheels = 4
    self.doors = 4
    self.enginetype = enginetype
  #OVERRIDE DELLA FUNZ EREDITATA
  def drive(self, speed):
    super().drive(speed)
    print("driving my", self.enginetype, "car at", self.speed)


class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if(hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0
    self.enginetype = enginetype
  #OVERRIDE DELLA FUNZ EREDITATA
  def drive(self, speed):
    super().drive(speed)
    print("driving my", self.enginetype, "motorcycle at", self.speed)

#ISTANZIAMO I PRIMI OGGETTI
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)


#ACCEDO ALLE LORO PROPRIETà : . notation
print(car1.doors)
print(car2.enginetype)
print(mc1.wheels)

#USO LA FUNCTION OVERRIDATA
car1.drive(50)
car2.drive(4)
mc1.drive(30)



#crea come posso avere different type of cars
#come ggiungo diverse funzioni come parcheggiare o fare inversione