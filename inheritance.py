

class vehicle:
    #Defining the attributes of the class
    engine = '4 cylinder boxer engine'
    body = 'coupe'
    fuel = 'unleaded fuel'
    number_wheels = 4


class airplane(vehicle):
    #Defining the child classes attributes that are unique to them
    number_of_wings = 2
    number_of_engines = 4

class motorcycle(vehicle):
    type_of_cycle = 'dirt bike'
    type_of_engine = '2-stroke'
    
    
