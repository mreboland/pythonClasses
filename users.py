"""Simulating a new user"""

# see newUser.py
# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.

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


# Moved to admin.py
# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

# class Privileges():
#     def __init__(self):
#         self.privileges = ["can add post", "can delete post", "can ban user"]

#     def showPrivileges(self):
#         print("\nThe admin has the following privileges:")
#         for privilege in self.privileges:
#             print(f"\t{privilege}")


# class Admin(User):
#     """Modeling a special user"""

#     def __init__(self, firstName, lastName, age, nationality):
#         super().__init__(firstName, lastName, age, nationality)
#         self.privileges = Privileges()
