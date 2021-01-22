# In OOP you write classes that represent real-world things and situations. You create objects based on these classes. When you write a class, you define the general behaviour that a whole category of objects can have.
# Making an object from a class is called instantiation, and you work with instances of a class.

# Creating and using a class
# Example we'll create a model of a dog (all kinds, not just one)
# We know all pet dogs have a name and age. We also know must dogs sit and roll over. We'll use those to create our class

# Here we are defining a class called Dog. By convention capitalized names refer to classes in python. There are no parenthese in the class definition because we're creating this class from scratch.
class Dog:
    # Writting a docstring to describe what this class does
    """A simple attempt to model a dog"""

    # A function that's part of a class is called a method. Everything learned about functions applies to methods as well. The only change is in how we call them.
    # The init method is a special method that Python runs automatically whenever we create a new instance based on the Dog class. Be careful of typos with the 2 underscores on both sides.
    # init was defined with 3 parameters. The self parameter must be included in the definition because python calls this method to create an instance of dog and will pass the self parameter. Every method call associated with an instance automatically passes self, which references the instance itself (gives the individual instance access to the attributes and methods in the class).
    # When we make an instance of Dog, python calls the init method from the Dog class. We pass Dog() a name and age as arguments. 'self' is passed automatically so we don't need to pass it.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # The two variables below with the prefix of self allows every method in the class to access those variables
        # The line self.name = name takes the value associated with the param 'name' and assigns it to the variable name, which is then attached to the instance being create. Same applies to 'ago'. Variables that are accessible through instances like this are called attributes.
        self.name = name
        self.age = age

    # These two methods don't need any additional info to run, so we define them with the parameter 'self'.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def rollOver(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
# Making an instance from a class
# Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells python how to make individual instances representing specific dogs

# Here we tell Python to create a dog with the provided name and age
# Python reads this line and calls the init method in Dog with the arguments we provided below. The init method in Dog creates an instance representing this particular dog and sets the name and age attributes using the values we provided. Python then returns an instance representing this dog which we assigned to myDog. We can usually assume that a cap name like Dog refers to a class while lowercase refers to a single instance created from a class.
myDog = Dog("Willie", 6)

# We access the attributes of an instance using dot notation. Python looks at the instance myDog and finds the attribute 'name' associated with it. This is the same attribute referred to as self.name in the class Dog.
print(f"My dog's name is {myDog.name}.")
print(f"My dog is {myDog.age} years old.")

# Calling methods
# After creating the instance from class Dog, we can use dot notation to call any method defined in Dog.
myDog.sit()
myDog.rollOver()

# Creating multiple instances
class Dog:
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def rollOver(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# We created two dogs. Each dog is a separate instance with its own set of attributes, capable of the same actions.
# Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class.
# We can create as many instance from one class as we need, as long as the name of the instance is a unique variable name, or if it occupies a unique spot in a list or dictionary.
myDog = Dog("Willie", 6)
yourDog = Dog("Lucy", 3)

print(f"\nMy dog's name is {myDog.name}.")
print(f"My dog is {myDog.age} years old.")
myDog.sit()

print(f"\nYour dog's name is {yourDog.name}.")
print(f"Your dog is {yourDog.age} years old.")
yourDog.sit()

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        """Init attr for restaurant name and cuisine"""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        
    def describeRestaurant(self):
        """Describing the restaurant"""
        print(f"The restaurant is called {self.restaurantName} and it serves {self.cuisineType.title()}.")

    def openRestaurant(self):
        """Simulating opening of restaurant"""
        print(f"{self.restaurantName.title()} is now open!")
        
restaurant = Restaurant("Japango", "Sushi")
print(restaurant.restaurantName)
print(restaurant.cuisineType)
restaurant.describeRestaurant()
restaurant.openRestaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.


restaurantA = Restaurant("restaurantA", "pizza")
restaurantB = Restaurant("restaurantB", "asian fusion")
restaurantC = Restaurant("restaurantC", "western")

restaurantA.describeRestaurant()
restaurantB.describeRestaurant()
restaurantC.describeRestaurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

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
        
userA = User("john", "doe", 55, "canadian")
userB = User("jane", "doe", 30, "german")

userA.describeUser()
userA.greetUser()

userB.describeUser()
userB.greetUser()