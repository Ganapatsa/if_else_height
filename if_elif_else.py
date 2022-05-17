# Students Marks
#DT FC SC TC FAIL

marks = int(input('Enter Marks:'))

if marks>=85 and marks <=100:
    print('Distinction')
elif marks>=65 and marks<85:
    print('First class')
elif marks>=35 and marks<65:
    print('Second class')
elif marks<35 and marks>=0:
    print('Failed')
else:
    print('Invalid number,please enter the range between 0 to 100')
