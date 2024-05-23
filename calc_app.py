# Training 

def addition(number_1, number_2):
    result = float(number_1) + float(number_2)
    total_calculations.append(f'{number_1} + {number_2} = {result}')
    return result


def subtraction(number_1, number_2):
    result = float(number_1) - float(number_2)
    total_calculations.append(f'{number_1} - {number_2} = {result}')
    return result


def multiplication(number_1, number_2):
    result = float(number_1) * float(number_2)
    total_calculations.append(f'{number_1} * {number_2} = {result}')
    return result


def division(number_1, number_2):
    try:
        result = float(number_1) / float(number_2)
        total_calculations.append(f'{number_1} / {number_2} = {result}')
        return result
    except ZeroDivisionError: # To make sure I don't get the / 0 error. https://docs.python.org/3/library/exceptions.html
        print('You are dividing by 0 which is invalid.')
        return None # Had to find a way online to get nothing as a return. https://www.w3schools.com/python/ref_keyword_none.asp


# Function for menu.
def options():
    print('\nOptions:')
    print('1 = calculate an addition.')
    print('2 = calculate a subtraction.')
    print('3 = calculate a multiplication.')
    print('4 = calculate a division.')
    print('5 = show calculations.')
    print('0 = quit.')


# Where all the calculations will be stored.
total_calculations = []

# Read existing calculations from 'equations.txt' file.
# Use defensive programming incase file is not found.
try:
    with open('equations.txt', 'r') as file:
        existing_calculations = set(line.strip() for line in file.readlines()) # To replace the adding calculations every time the file is closed and reopened.
        total_calculations.extend(existing_calculations)
except FileNotFoundError as error:
    print('The file that you are trying to open does not exist.')
    print(error)
    print('This is probably because it is the first time you are opening the file and have not made any calculations yet.')

print('\nThis program will calculate for you either an addition, subtraction, multiplication, or a division and store the calculations on a file: \'equations.txt\'. ')
print('This program can also read calculations from the \'equations.txt\' file whenever they are added. (option 5.) ')
print('When you are finished with your calculations, please use the quit option. (option 0.) ')
choice = '6'
# Using defensive programming in each calculation choice to avoid unexpected events.
options()
while choice != '0':
    choice = input('Please enter your choice: ')
    if choice == '1':
        while True:
            number_1 = input('\nYou have chosen addition.\nPlease enter your first number: ')
            try:
                float(number_1)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        while True:    
            number_2 = (input('Please enter your second number: '))
            try:
                float(number_2)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        result = addition(number_1, number_2)
        print('The answer to your addition is:', result, '\n')
        options()
    elif choice == '2':
        while True:
            number_1 = input('\nYou have chosen subtraction.\nPlease enter your first number: ')
            try:
                float(number_1)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        while True:    
            number_2 = (input('Please enter your second number: '))
            try:
                float(number_2)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        result = subtraction(number_1, number_2)
        print('The answer to your subtraction is:', result, '\n')
        options()
    elif choice == '3':
        while True:
            number_1 = input('\nYou have chosen multiplication.\nPlease enter your first number: ')
            try:
                float(number_1)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        while True:    
            number_2 = (input('Please enter your second number: '))
            try:
                float(number_2)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        result = multiplication(number_1, number_2)
        print('The answer to your multiplication is:', result, '\n')
        options()
    elif choice == '4':
        while True:
            number_1 = input('\nYou have chosen division.\nPlease enter your first number: ')
            try:
                float(number_1)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        while True:    
            number_2 = (input('Please enter your second number: '))
            try:
                float(number_2)
                break
            except ValueError:
                print('You have not entered a valid number. Please enter a valid number:')
        result = division(number_1, number_2)
        if result is not None: # The Zero division return of def division.
            print('The answer to your division is:', result, '\n')
        options()
    elif choice == '5':
        print('\nCalculations:')
        for calculation in total_calculations:
            print(calculation.strip())
        options()
    elif choice == '0':
        print('')
    else:
        print('Unrecognized option. Please enter a valid option.')
        options()

# Writing new calculations to 'equations.txt' file.
with open('equations.txt', 'w') as file: # I was first using the a+ method but the calculations were duplicating on the txt. file so had to backtrack.    
    for calculation in total_calculations:
        file.write(calculation.rstrip() + '\n') # Had to use strip to make sure there aren't spacing in the text file.
