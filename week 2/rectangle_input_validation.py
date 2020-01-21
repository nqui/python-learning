lengthA = float(input('enter the length of rectangle A that is in [5,12]:'))
widthA = float(input('enter the width of rectangle A that is in [1, 20]:'))

if lengthA < 5 or lengthA > 12: 
    print('the length is out of bounds')
    if lengthA < 5:
        print('the length is too small')
    else:
        print('the length is too big')
elif widthA < 1 or widthA > 20:
    print('the width is out of bounds')
    if widthA < 1:
        print('the width is too small')
    else:
        print('the width is too big')
else:
    AreaA = lengthA * widthA
    print('the area is ', format(AreaA, '.3f'), 'sq. m')