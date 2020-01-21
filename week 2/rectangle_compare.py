lengthA = float(input('enter length of rectangle A: '))
widthA = float(input('enter width of rectangle A:'))

lengthB = float(input('enter length of rectangle B: '))
widthB = float(input('enter width of rectangle B:'))

areaA = lengthA * widthA
areaB = lengthB * widthB

if areaA > areaB:
    print('rectangle a is bigger than rectangle b')
elif areaB > areaA:
    print('rectangle b is bigger than rectangle a')
else:
    print('both rectangles have an equal area')
print('rectangle A area: ', format(areaA, '.3f'), 'sq. m')
print('rectangle B area: ', format(areaB, '.3f'), 'sq. m')