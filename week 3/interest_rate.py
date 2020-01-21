import math

interest_rate = 0
years = 0 

while interest_rate < 1 or interest_rate > 2.5:
    interest_rate = float(input('enter an interest rate between 1 - 2.5: '))
while years < 10 or years > 15:
    years = float(input('enter a number of years between 10 - 15: '))

print('interest rate:',interest_rate)
print('number of years:',years)

print('future value($) \t present value ($)')
for future in range(10000, 100000, 20000):
    present = future / math.pow((1 + interest_rate / 100), years)
    print(format(future, ',.2f'), '\t \t', format(present, ',.2f'))