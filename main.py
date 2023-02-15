#Erik Miller Intro to Programming Week 8 Assignment

#Create vehicle class
class Vehicle:
  #Create function that can be called by a vehicle to set make
  def setVehicleMake(self, make):
    self.str_VehicleMake = make
    
  #Create function that can be called by a vehicle to set model
  def setVehicleModel(self, model):
    self.str_VehicleModel = model
  #Create function that can be called by a vehicle to return make
  def getVehicleMake(self):
    return self.str_VehicleMake
  #Create function that can be called by a vehicle to return model
  def getVehicleModel(self):
    return self.str_VehicleModel

#Create a Car class that inherits from Vehicle.
class Car(Vehicle):
  #Create function that can be called by a car to set number of doors.
  def setCarDoors(self, doors):
    self.str_CarDoor = (doors)
    
  #Create function that can be called by a car to get number of doors.
  def getCarDoors(self):
    return self.str_CarDoor

#Create Truck class that inherits from Vehicle
class Truck(Vehicle):
  #Create function that sets length of truck bed.
  def setBedLength(self, bedLength):
    self.str_BedLength = bedLength
  #Create function that gets length of truck bed.
  def getBedLength(self):
    return self.str_BedLength

#Send introduction message to user
print("Welcome to E0m00p2's Virtual Garage")
print("")
#Set selection variable for loop so that program repeats until you select to quit via inputting 3.
selection = 0
while int(selection) < int(3):
  selection = input("Enter 1 to make a car, 2 to make a truck, or 3 to quit: ")
  print("")
  #If user selects 1, create a new car and ask for user to input make, model, and car door number, using functions made in vehicle and car class. 
  #Print new cars details.
  if (selection == '1'):
    new_car = Car()
    strMake = input("Please enter the car make:")
    new_car.setVehicleMake(strMake)
    strModel = input("Please enter the car model:")
    new_car.setVehicleModel(strModel)
    strDoors = input("Please enter the number of doors:")
    new_car.setCarDoors(strDoors)
    print("")
    print(f"The number of doors: {new_car.getCarDoors()}")
    print(f"The make is: {new_car.getVehicleMake()}")
    print(f"The model is: {new_car.getVehicleModel()}")
    print("You car has been added to the Garage.")
  #If user selects 2, create a new truck and ask for user to input make, model, and truck bed length number, using functions made in vehicle and truck class. 
  #Print new truck details.
  elif (selection == '2'):
    new_truck = Truck()
    strMake = input("Please enter the truck make:")
    new_truck.setVehicleMake(strMake)
    strModel = input("Please enter the truck model:")
    new_truck.setVehicleModel(strModel)
    strDoors = input("Please enter the bed length:")
    new_truck.setBedLength(strDoors)
    print("")
    print(f"The bed length is: {new_truck.getBedLength()}")
    print(f"The make is: {new_truck.getVehicleMake()}")
    print(f"The model is: {new_truck.getVehicleModel()}")
    print("Your truck has been added to the Garage.")
  #If any number other than 1 or 2, print thank you. If 3 or above, loop is exited and program ends.
  else:
    print("")
    print("Thank you for using E0m00p2's Garage.")
  print("")
