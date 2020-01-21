grade = int(input('enter your grade percentage number: '))

if grade >= 80 and grade <= 100:
    print('your grade is: A')
elif grade >= 70 and grade < 80:
    print('your grade is: B')
elif grade >= 60 and grade <= 60:
    print('your grade is: C')
elif grade >= 50 and grade <= 59:
    print('your grade is: D')
elif grade < 50:
    print('your grade is: F')
else:
    print('invalid grade input')