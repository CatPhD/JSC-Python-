import math

def calcConeVolume(radius, height):
    volume = (math.pi * radius **2 * height)/3
    return volume

radius = float(input('Enter radius of a cone: '))
height = float(input('Enter height of a cone: '))
volume = calcConeVolume(radius, height)

print('The volume is', volume)
