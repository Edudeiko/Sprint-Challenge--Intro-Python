# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    '''Base class for GroundVehicle and FlightVehicle'''
    pass

class GroundVehicle(Vehicle):
    '''Base class for Car and Motorcycle'''
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class FlightVehicle(Vehicle):
    '''Base class for Airplane and Starship'''
    pass

class Starship(FlightVehicle):
    '''Base class for Airplane'''
    pass

class Airplane(FlightVehicle):
    pass
