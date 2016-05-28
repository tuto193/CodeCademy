class Shape( object ):
    """Makes shapes!"""
    def __init__( self, number_of_slides ):
        self.number_of_slides = number_of_slides

#add own code below
class Triangle( Shape ):
    """Has 3 sides"""
    def __init__( self, side1, side2, side3 ):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
