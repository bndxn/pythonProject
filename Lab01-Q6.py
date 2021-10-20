'''Sort three numbers
Write a program using if-statements that takes as input three numbers in random order.
Print out the three numbers in descending order.'''

a, b, c = input('Enter three numbers :').split()
a, b, c = int(a), int(b), int(c)

# Break into two main cases
# where a is greater than or less than b

if a > b:
    if c > a:
        print(c, a, b)  # first sub-case, c is the biggest
    elif c < b:
        print(a, b, c)  # or c is is the smallest
    elif a > c > b:
        print(a, c, b)  # or c is in-between a and b

# where a is less than b

if a < b:
    if c > b:
        print(c, b, a)  # c is biggest
    elif c < a:
        print(b, a, c)  # c is smallest
    elif a < c < b:
        print(b, c, a)  # c is in-between a and b

# Verify password!

password = 'hackingthematrix'
p = input('Type in your password:')
if p == password:
    print('Password accepted.')
else:
    print('Wrong password.')

# Calculate UCL grade

g = input('Type in grade as number :')
g = int(g)

if g <= 100 and g >= 0:
    if g >= 70:
        print('Distinction.')
    elif g >= 50:
        print('Pass.')
    elif g >= 0:
        print('Fail. ')
else:
    print('Incorrect value entered. Please enter in a value between 0 and 100 (inclusive).')


