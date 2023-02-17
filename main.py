#Erik Miller Intro to Programming Week 8 Assignment
import tkinter as tk

class Vehicle:
    def setVehicleMake(self, make):
        self.str_VehicleMake = make
    
    def setVehicleModel(self, model):
        self.str_VehicleModel = model
        
    def getVehicleMake(self):
        return self.str_VehicleMake
        
    def getVehicleModel(self):
        return self.str_VehicleModel

class Car(Vehicle):
    def setCarDoors(self, doors):
        self.str_CarDoor = doors
        
    def getCarDoors(self):
        return self.str_CarDoor

class Truck(Vehicle):
    def setBedLength(self, bedLength):
        self.str_BedLength = bedLength
        
    def getBedLength(self):
        return self.str_BedLength

def create_car():
    new_car = Car()
    strMake = make_entry.get()
    new_car.setVehicleMake(strMake)
    strModel = model_entry.get()
    new_car.setVehicleModel(strModel)
    strDoors = doors_entry.get()
    new_car.setCarDoors(strDoors)
    result_label.config(text=f"The number of doors: {new_car.getCarDoors()}\nThe make is: {new_car.getVehicleMake()}\nThe model is: {new_car.getVehicleModel()}\nYour car has been added to the Garage.")

def create_truck():
    new_truck = Truck()
    strMake = make_entry.get()
    new_truck.setVehicleMake(strMake)
    strModel = model_entry.get()
    new_truck.setVehicleModel(strModel)
    strLength = length_entry.get()
    new_truck.setBedLength(strLength)
    result_label.config(text=f"The bed length is: {new_truck.getBedLength()}\nThe make is: {new_truck.getVehicleMake()}\nThe model is: {new_truck.getVehicleModel()}\nYour truck has been added to the Garage.")

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("E0m00p2's Virtual Garage")

# Create labels
make_label = tk.Label(root, text="Make:")
model_label = tk.Label(root, text="Model:")
doors_label = tk.Label(root, text="Doors:")
length_label = tk.Label(root, text="Length:")
result_label = tk.Label(root, text="")

# Create entry fields
make_entry = tk.Entry(root)
model_entry = tk.Entry(root)
doors_entry = tk.Entry(root)
length_entry = tk.Entry(root)

# Create buttons
car_button = tk.Button(root, text="Create Car", command=create_car)
truck_button = tk.Button(root, text="Create Truck", command=create_truck)
quit_button = tk.Button(root, text="Quit", command=quit_program)

# Add labels, entry fields, and buttons to the window
make_label.grid(row=0, column=0)
make_entry.grid(row=0, column=1)
model_label.grid(row=1, column=0)
model_entry.grid(row=1, column=1)
doors_label.grid(row=2, column=0)
doors_entry.grid(row=2, column=1)
length_label.grid(row=3, column=0)
length_entry.grid(row=3, column=1)
car_button.grid(row=4, column=0)
truck_button.grid(row=4, column=1)
result_label.grid(row=5, column=0, columnspan=2)
quit_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
