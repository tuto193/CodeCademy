class Car( object ):
    condition = "new"
    def __init__( self, model, color, mpg ):
        self.model = model
        self.color = color
        self.mpg = mpg
    def display_car( self ):
        print "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg ) 
    def drive_car( self ):
        self.condition = "used"

class ElectricCar( Car ):
    def __init__( self, model, color, mpg,  battery_type ):
        #Must initialise Parent Class to inherit attributes and add the remaining.
        Car.__init__( self, model, color, mpg )
        self.battery_type = battery_type

my_car = ElectricCar( "DeLorean", "silver", 88, "molten salt" )

