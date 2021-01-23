# Importing multiple classes from a module
# We can import as many classes as we need into a program file

# We import multiple classes from a module by separating each class with a comma
# Once imported, we are free to use each class as needed
from cars import Car, ElectricCar

myBeetle = Car("volkswagen", "beetle", 2019)
print(myBeetle.getDescriptiveName())

myTesla = ElectricCar("tesla", "roadster", 2019)
print(myTesla.getDescriptiveName())

# Importing an entire module
# We can also import an entire module and then access the classes we need by using dot notation. This approach is simple and results in code that is easy to read.
print("\n")
# Here we import the entire cars module and we access it by using moduleName.ClassName syntax
import cars

myBeetle = cars.Car("volkswagen", "beetle", 2019)
print(myBeetle.getDescriptiveName())

myTesla = cars.ElectricCar("tesla", "roadster", 2019)
print(myTesla.getDescriptiveName())

# Importing all classes from a module
# from moduleName import *

# This method is not recommended for a few reasons.
# One with this approach it's unclear which classes we're using from the module. This results in confusion with names in the file. It can result in importing another module that has the same naming for classes which will conflict and or overwrite your classes. This can lead to difficult dianoses.

# Importing a module into a module
# When our module in electricCars.py is import Car from cars, we now need to import both the original car module, and the new electricCars module into our file to use them

print("\n", "module in module")

# Because we split ElectricCar (and Battery) from cars.py we need to import both to have access to them
from cars import Car
from electricCars import ElectricCar

myBeetle = cars.Car("volkswagen", "beetle", 2019)
print(myBeetle.getDescriptiveName())

myTesla = cars.ElectricCar("tesla", "roadster", 2019)
print(myTesla.getDescriptiveName())

# Using aliases
# Like in chapter 8, we can give aliases to our imported modules

# from electricCars import ElectricCar as EC
# myTesla = EC(....)
