import math

for n in range(1, 6):
    answer = math.sqrt(n)
    print(n, '\t', format(answer, '.3f'))
print('=' * 14)
for n in range(12, 3, -2):
    answer = math.sqrt(n)
    print(n, '\t', format(answer, '.3f'))