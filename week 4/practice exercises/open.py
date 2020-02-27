import math

def sincostan(x):
    sin = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    print("sin: ", format(sin,'.3f'), "cos: ", format(cos,'.3f'), "tan: ", format(tan,'.3f'))

sincostan(3)

def maxmin(x,y,z):
    if(x>y):
        if(x>z):
            print(z)
    if(y>x):
        if(y>z):
            print(y)
    if(z>x):
        if(z>y):
            print(z)

maxmin(5,14,7)


def getvalues():
    def rect(x,y):
        area = x * y
        print("the area is {area}")
    x = 0
    y = 0
    while((x>=1 or x<=10) and (y>=1 or y<=10)):
        x = int(input('input the length: '))
        y = int(input('input the width: '))
    rect(10,10)
getvalues()