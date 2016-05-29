class Employee( object ):
    """Models real-life employees!"""
    def __init__( self, employee_name ):
        self.employee_name = employee_name

    def calculate_wage( self, hours ):
        self.hours = hours
        return hours * 20.00

#add my own code underneath
class PartTimeEmployee( Employee ):
    """Only works part time"""
    def calculate_wage( self, hours ):
        self.hours = hours
        return hours * 12.00
    def full_time_wage( self, hours ):  #super( Child, self ).parent_method( second argument)
        return super( PartTimeEmployee, self).calculate_wage( hours )

milton = PartTimeEmployee( "Milton" )
print milton.full_time_wage( 10 )
