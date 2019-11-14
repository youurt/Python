
# 9-10

class Restaurant():
    """A class describing a Restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print("The Restaurant " + self.restaurant_name.title() + " has " + self.cuisine_type.title() + " Cuisine!")
     
    def open_restaurant(self):
        """Print that the restaurant is open."""
        print("The Restaurant " + self.restaurant_name.title() + " is open!")
        
    def read_number_served(self):
        """Reads how many items are been served."""
        print("This restaurant has " + str(self.number_served) + " items served.")
        
    def set_number_served(self, served):
        """Sets the number of served items. The initial Value is 0!"""
        self.number_served = served
        
    def increment_number_served(self, update):
        """Updates the number of served items."""
        self.number_served += update     
        
class IceCreamStand(Restaurant):
    """A class describing an Ice Cream Stand, which is a child of a Restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class.
        Then initialize attributes specific."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanillia', 'chocolate', 'banana']
        
    def display_flavors(self):
        """Print the flavors of the ice cream."""
        print("This restaurant serves " + str(self.flavors) + " Ice Cream!")
        
my_ice_store = IceCreamStand('Luna Ice', 'Ice Cream')
my_ice_store.display_flavors()
