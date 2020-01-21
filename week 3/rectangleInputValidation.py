lengthA = float(input('Enter the length in the interval [5, 12]: '))
while lengthA < 5 or lengthA > 12:
    lengthA = float(input('\nInput length is out of bounds.' + 
        '\nEnter the length in the interval [5, 12]: '))

widthA = float(input('Enter the width in the interval (10, 30): '))
while widthA <= 10 or widthA >= 30:
    widthA = float(input('\nInput width is out of bounds.' + 
        '\nEnter the width in the interval [10, 30]: '))

areaA = lengthA * widthA
print('The area of rectangle A is:', format(areaA,'.3f'),'sq m.')