import math
MASS = 20
GRAVITY = 9.8

def main():
    velocity = float(input('enter a velocity: '))
    height = float(input('enter a height: '))
    KineticEnergy(velocity)
    PotentialEnergy(height)

def KineticEnergy(velocity):
        kinetic_energy = 0.5 * MASS * math.pow(velocity, 2)
        print(kinetic_energy)
    
def PotentialEnergy(height):
        potential_energy = MASS * GRAVITY * height
        print(potential_energy)

main()