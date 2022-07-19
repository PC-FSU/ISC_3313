from math import pi

def surface_area(radius):
    '''
    Calculate surface area of a sphere
    '''
    return 4 * pi * radius**2 

def volume(radius):
    '''
    Calculate volume of a sphere
    '''
    print('calculating volume')
    return (4/3) * pi * radius**3 

def circumference(radius):
    '''
    Calculate circumference of a sphere
    '''
    return 2 * pi * radius
