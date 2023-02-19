marks = int(input('please enter your marks : '))

if marks > 90 : 
    print('Your grade is A')
elif marks > 80 and marks <= 90: 
    print('your grade is B')
elif marks >=60 and marks <= 80:
    print('your grade is C')
elif marks > 33 and marks <= 60:
    print('your grade is D')
else:
    print('your grade is F+')