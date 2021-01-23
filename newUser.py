# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.

# from users import Admin

# admin = Admin("jane", "doe", 27, "french")

# admin.describeUser()
# admin.privileges.showPrivileges()


# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

from admin import Admin

admin = Admin("jane", "doe", 27, "french")

admin.describeUser()
admin.privileges.showPrivileges()
