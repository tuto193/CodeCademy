#Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #add own methods
    def description(self):
        print self.name
        print self.age

hippo = Animal("Hippo", 9)
hippo.description
