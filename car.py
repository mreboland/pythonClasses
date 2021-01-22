# Working with classes and instances
# Once a Class is written, most of the time spent is with instances created
# with that Class. One of the first tasks we'll want to do is modify the
# attributes associated with a particular instance.
# We can modify the attributes of an instance directly or write methods that 
# update attributes in specific ways

class Car:
    """A simple attempt to represent a car"""
    
    # Exact same setup as our Dog example
    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        # Return instead of print here, sends the data to the call
        return longName.title()
    
# myNewCar = Car("audi", "a4", 2019)
# print(myNewCar.getDescriptiveName())

# To make the class more interesting, we'll add an attribute that changes over
# time. We'll use a cars mileage to do so.

# Setting a default value for an attribute
class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # When an instance is created, attributes can be defined without being passed in as parameters. They can be defined in the init and are assigned a default value
        # Here we create the odometer with a initial value of 0
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()
    
    # We created a method to read the odometer
    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")


myNewCar = Car("audi", "a4", 2019)
print(myNewCar.getDescriptiveName())
myNewCar.readOdometer()

# Modifying attribute values
# We can change an attribute's value in three ways:

# Directly, through an instance:

# The simplest way is to modify the value of an attribute through the instance
# We use dot notation to access the attribute odometerReading and we set the value equal to what we want
myNewCar.odometerReading = 23
# Showing the change
myNewCar.readOdometer()


# Modifying an attribute's value through a method

# It can be helpful to have methods that update certain attributes for you.
# Instead of accessing the attribute directly, we pass the new value to a
# method that handles the updating internally
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
        
    # Here we created a method that takes in a mileage parameter and assigns
    # it to self.odometerReading which will update the value when we pass
    # through an argument
    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attempts to roll the odometer back."""
        # We can extent the method to do additional work to prevent rolling
        # back the odometer.
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

myNewCar = Car("audi", "a4", 2019)
print(myNewCar.getDescriptiveName())

# Here we call updateOdometer and give it an argument of 55. This value is
# passed into the method, updateOdometer which updates the odometerReading
# value
myNewCar.updateOdometer(55)
# We then print the odometer to see its new value.
myNewCar.readOdometer()

# Testing the if statement for roll back (mileage is currently 55)
myNewCar.updateOdometer(25)

# Increment an attribute's value through a method

# Sometimes we'll want to increment an attribute's value by a certain amount
# rather than set an entirely new value. Say we buy a used car and put 100
# miles on it between the time we buy it and the time we register it.
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
    
    # We create a new method that takes in a number of miles and adds this
    # value to self.odometerReading
    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        # Doing some self coding to reject negative miles
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't have negative miles...")

# We create a used car
myUsedCar = Car("subaru", "outback", 2015)
print(myUsedCar.getDescriptiveName())

# We set its odometer to 23,500 (remember underscores can be used like commas)
# by calling updateOdometer. This is the car's initial mileage.
myUsedCar.updateOdometer(23_500)
myUsedCar.readOdometer()

# After driving it 100 miles we want to add it to our base milage we set above
# so we call incrementOdometer and pass it 100 to update our mileage
myUsedCar.incrementOdometer(100)
myUsedCar.readOdometer()

# Negative miles test
myUsedCar.incrementOdometer(-100)
# Miles stayed the same
myUsedCar.readOdometer()

# Note: You can use methods like this to control how users of your program
# update values such as an odometer reading, but anyone with access to the
# program can set the odometer reading to any value by accessing the attribute
# directly. Effective security takes extreme attention to detail in addition
# to basic checks like those shown here.

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.
class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        """Init attr for restaurant name and cuisine"""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        self.numberServed = 0

    def describeRestaurant(self):
        """Describing the restaurant"""
        print(
            f"The restaurant is called {self.restaurantName} and it serves {self.cuisineType.title()}.")

    def openRestaurant(self):
        """Simulating opening of restaurant"""
        print(f"{self.restaurantName.title()} is now open!")
        
    def setNumberServed(self, customers):
        """Updating the base number of customers served"""
        if customers >= 0:
            self.numberServed = customers
        else:
            print("You can't serve a negative amount customers")
            
    def incrementNumberServed(self, served):
        """Adding served customers to base customers served"""
        if served >= 0:
            self.numberServed += served
        else:
            print("You can't reduce the amount of customers served!")


restaurant = Restaurant("Japango", "Sushi")
print(restaurant.numberServed)
restaurant.numberServed = 10
print(restaurant.numberServed)

restaurant.setNumberServed(15)
print(restaurant.numberServed)

restaurant.incrementNumberServed(5)
print(restaurant.numberServed)

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.
class User:
    def __init__(self, firstName, lastName, age, nationality):
        """Creating a user"""
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.nationality = nationality
        self.loginAttempts = 0

    def describeUser(self):
        print(f"\n{self.firstName.title()} {self.lastName.title()}:")
        print(f"\tAge: {self.age}")
        print(f"\tNationality: {self.nationality.title()}")

    def greetUser(self):
        print(f"Hello {self.firstName.title()}! How are you today?")
        
    def incrementLoginAttempts(self):
        """Counting the amount of attempts made at logging in"""
        self.loginAttempts += 1
        
    def resetLoginAttempts(self):
        """Resetting login attempts"""
        self.loginAttempts = 0

userA = User("john", "doe", 55, "canadian")

userA.incrementLoginAttempts()
userA.incrementLoginAttempts()
userA.incrementLoginAttempts()
print(userA.loginAttempts)

userA.resetLoginAttempts()
print(userA.loginAttempts)
