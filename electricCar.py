# Inheritance
# You don't always have to start from scratch when writing a class. If the class you're writting is a specialized version of another class you wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, the new class is the child class. The child class can inherit any or all of the attributes and methods of its parent, but it's also free to define new attributes and methods of its own.

# The init method for a child class
# When you write a new class based on an existing class, you'll often want to call the init method from the parent class. This will init any attributes and methods in the parent available to the child.
class Car:
    # Here with start with the Car class we built earlier. When we create a chile class, the parent class must be a part of the current file and must appear before the child class in the file.
    
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't have negative miles...")
            
# Here we defined the child class. The parent class Car, must be included in the parenthesis of the child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    
    # The init method takes in the info required to make a Car instance
    # The parameters must match the parent init
    def __init__(self, make, model, year):
        """Init attributes of the parent class."""
        
        # The super() function is a special function that allows you to call a method from the parent class. This line tells python to call the init method from Car, which gives an ElectricCar instance all the attributes defined in that method. The name super comes from a convention of calling the parent class a superclass and the child class a subclass
        super().__init__(make, model, year)
    
# We test whether the inheritance is working properly by trying to create an electric car with the same kind of info we'd provide when making a regular car.
# We make an instance of the ElectricCar class. It calls the init method defined in ElectricCar which in turn tells python to call the init method defined in the parent, Car class.
myTesla = ElectricCar("tesla", "model s", 2019)
print(myTesla.getDescriptiveName())

# Defining attributes and methods for the child class
# Once we have a child class that inherits from a parent, we can add any new attributes and methods necessary to differentiate them.
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't have negative miles...")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """Init attributes of the parent class."""
        """Then init attributes specific to an electric car."""
        super().__init__(make, model, year)
        # Here we add a new attribute for battery size and gave it an initial value
        # This attribute will be associated will all instances of ElectricCar but not Car
        self.batterySize = 75
        
    # Added a basic method to describe battery size
    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.batterySize}-kWh battery.")
        
myTesla = ElectricCar("tesla", "model s", 2019)
print(myTesla.getDescriptiveName())
myTesla.describeBattery()

# There's no limit to how much you can specialize the electric car class. We can add as many attributes and methods as we need to properly model an electric car.
# An attribute or method that could belong to any car, rather than one that's specific to electric should be added to the parent, Car class. This is so it's accessible across the board.

# Overriding methods from the parent class
# We can overide any moethod from the parent class that doesn't fit what we're trying to model with the child class. We do this by defining a method in the child with the same name as the parent

# Say the class Car had a method called fillGasTank(). This method is meaningless for an electric car so we'd want to override this method.
class ElectricCar(Car):
    # --snip--
    
    # Now if someone tries to call fillGasTank() with an electric car instance, python will ignore the method fillGasTank() in Car and run the below code instead
    def fillGasTank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
    
# With inheritance, you can make your child classes retain what you need and override anything you don't need from the parent class.

# Instances as attributes
# When modeling something from the real world, you may find that you're adding more and more detail to a class. You'll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.

# Using electric car, we might notice that we are adding too many attributes and methods specific to its battery.
# We'll move those methods to it's own battery class
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't have negative miles...")
            
# Here we define a new class battery that doesn't inherit from any other class (no super()).
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    # Our init method has one param, which has a default value if no value is given
    def __init__(self, batterySize=75):
        """Init the battery's attributes."""
        self.batterySize = batterySize
        
    # This method was originally in ElectricCar class and we moved it here
    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.batterySize}-kWh battery.")
    
    # Basic method that gives us a range in miles depending on battery size
    def getRange(self):
        """Print a statement about the range this battery provides."""
        if self.batterySize == 75:
            range = 260
        elif self.batterySize == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Init attributes of the parent class."""
        super().__init__(make, model, year)
        # We have an attribute here that tells python to create (as we are calling Battery class) a new instance of Battery which gives us a default size of 75 (because we did not specify a value). We assign that instance to the attribute self.battery. This will happen everytime the init method is called. Any electric car instance will now have a Battery instance created automatically.
        self.battery = Battery()
        
myTesla = ElectricCar("tesla", "model s", 2019)
print(myTesla.getDescriptiveName())
# We create an electric car and assign it to the variable myTesla. When we want to describe the battery, we need to work through the car's battery attribute from the ElectricCar class (self.battery = Battery() -> self.battery = batterySize which defaults to 75). The self.battery holds the entire class of Battery and we access battery using dot notation learned earlier.
myTesla.battery.describeBattery()

# Breaking battery from electric car class seems like a lot of work however it allows us to expand the details of the battery specifically without cluttering up the ElectricCar class.
# Under battery we added a range method to see how far a battery can go
myTesla.battery.getRange()

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work
# just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        """Init attr for restaurant name and cuisine"""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        """Describing the restaurant"""
        print(
            f"The restaurant is called {self.restaurantName} and it serves {self.cuisineType.title()}.")

    def openRestaurant(self):
        """Simulating opening of restaurant"""
        print(f"{self.restaurantName.title()} is now open!")
        
        
class IceCreamStand(Restaurant):
    """Modeling an ice cream stand"""
    
    def __init__(self, restaurantName, cuisineType):
        """Init attributes of parent class."""
        super().__init__(restaurantName, cuisineType)
        self.flavours = ["chocolate", "vanilla", "mint chocolate chip"]
        
    def flavoursOffered(self):
        print("\nThe flavours on offer are:")
        for flavour in self.flavours:
            print(f"\t{flavour.title()}")
        
iceCreamStand = IceCreamStand("milky", "ice cream")
iceCreamStand.describeRestaurant()
iceCreamStand.flavoursOffered()


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class User:
    def __init__(self, firstName, lastName, age, nationality):
        """Creating a user"""
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.nationality = nationality

    def describeUser(self):
        print(f"\n{self.firstName.title()} {self.lastName.title()}:")
        print(f"\tAge: {self.age}")
        print(f"\tNationality: {self.nationality.title()}")

    def greetUser(self):
        print(f"Hello {self.firstName.title()}! How are you today?")
        
class Admin(User):
    """Modeling a special user"""
    def __init__(self, firstName, lastName, age, nationality):
        super().__init__(firstName, lastName, age, nationality)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def showPrivileges(self):
        print("\nThe admin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
        
admin = Admin("billy", "bob", 25, "canadian")
admin.describeUser()
admin.showPrivileges()

# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class User:
    def __init__(self, firstName, lastName, age, nationality):
        """Creating a user"""
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.nationality = nationality

    def describeUser(self):
        print(f"\n{self.firstName.title()} {self.lastName.title()}:")
        print(f"\tAge: {self.age}")
        print(f"\tNationality: {self.nationality.title()}")

    def greetUser(self):
        print(f"Hello {self.firstName.title()}! How are you today?")


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def showPrivileges(self):
        print("\nThe admin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    """Modeling a special user"""

    def __init__(self, firstName, lastName, age, nationality):
        super().__init__(firstName, lastName, age, nationality)
        self.privileges = Privileges()
        
        
admin = Admin("billy", "bob", 25, "canadian")
admin.describeUser()
admin.privileges.showPrivileges()


# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"\n{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't have negative miles...")
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, batterySize=75):
        """Init the battery's attributes."""
        self.batterySize = batterySize

    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.batterySize}-kWh battery.")

    def getRange(self):
        """Print a statement about the range this battery provides."""
        if self.batterySize == 75:
            range = 260
        elif self.batterySize == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
        
    def upgradeBattery(self):
        if self.batterySize == 75:
            self.batterySize = 100
        else:
            print("Your battery is already the max size offered.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Init attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


myTesla = ElectricCar("tesla", "model s", 2019)
print(myTesla.getDescriptiveName())
# To update the default battery size we can do:
# myTesla.battery.batterySize = 100

myTesla.battery.describeBattery()
myTesla.battery.getRange()

myTesla.battery.upgradeBattery()
myTesla.battery.getRange()
