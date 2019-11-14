
class Privileges():
    """A class for privileges."""
   
    def __init__(self, privileges=[]):
        self.privileges = privileges

    
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- No privileges.")
