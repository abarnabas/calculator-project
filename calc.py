#5-Function Calculator
def calculate():
    operation = input('''
Welcome! Please type in the math operation you would like to calculate:
+ to Add
- to Subtract
* to Multiply
/ to Divide
^ for Exponents
log for Logs
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '^':
        print('{} ** {} ='.format(number_1, number_2))
        print(number_1 ** number_2)
    else:
        print('Invalid Input.')

    again()

def again():
    calc_again = input('''
Would you like to continue calculating? Please type Y or N
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Thank you for using our calculator!')
    else:
        again()

calculate()