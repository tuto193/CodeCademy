class Employee( object ):
    """Models real-life employees!"""
    def __init__( self, employee_name ):
        self.employee_name = employee_name

    def calculate_wage( self, hours ):
        self.hours = hours
        return hours * 20.00

#add my own code underneath

