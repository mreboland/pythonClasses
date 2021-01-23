# Importing classese
# As we add more functionality to our classes, our files can very long, even when using inheritance properly. As such we should move them into their own modules.

# Importing a single class
from cars import Car

# After importing the module cars, we can use the class Car from it as if the class was in this file
myNewCar = Car("audi", "a4", 2019)
print(myNewCar.getDescriptiveName())

myNewCar.odometerReading = 23
myNewCar.readOdometer()