# Storing multiple classes in a module
# We can store as many classes as we need in a single module, although each class in a module should be related somehow.
# We added the classes Battery and ElectricCar to cars.py as they are related

from cars import ElectricCar

# As if the class was in the file, once we import it, we can use it as normal
myTesla = ElectricCar("tesla", "model s", 2019)

print(myTesla.getDescriptiveName())
myTesla.battery.describeBattery()
myTesla.battery.getRange()