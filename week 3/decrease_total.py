import math

a = 1000
for n in range(20, 9, -1):
    a = a - math.pow(n, 2)
    print(n, '\t', format(a, '9.2f')) # format(var, 'padding.decimalSpacesf')