# define the main function
def main():
    name = input('what is your name? ')
    print(f"Hello {name.title()}")
    while True:
        
        print('what operation do you want to perform')
        print('1.addition')
        print('2.substraction')
        print('3.multiplication')
        print('4.division')
        print('5.exit')

        user_input = int((input('choose any of operation: ')))

        # enter any operation 
        if user_input == 1:
            num_1 = input('x: ')
            num_2 = input('y: ')
            result = additon(num_1, num_2)
            print(f'{num_1} + {num_2} = {result}')

        elif user_input == 2:
            num_1 = input('x: ')
            num_2 = input('y: ')
            result = substraction(num_1, num_2)
            print(f'{num_1} - {num_2} = {result}')

        elif user_input == 3:
            num_1 = input('x: ')
            num_2 = input('y: ')
            result = multiplication(num_1, num_2)
            print(f'{num_1} - {num_2} = {result}')

        elif user_input == 4:
            num_1 = input('x: ')
            num_2 = input('y: ')
            result = division(num_1, num_2)
            print(f'{num_1} - {num_2} = {result}')

        elif user_input == 5:
            break
        
    
# define the operation function
def additon(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print('ENTER AN INTEGER')

def substraction(x, y):
    try:
        return float(x) - float(y)
    except:
        print('ENTER AN INTEGER')

def multiplication(x, y):
    try:
        return float(x) * float(y)
    except:
        print('ENTER AN INTEGER')

def division(x, y):
    try:
        return float(x) / float(y)
    except:
        print('ENTER AN INTEGER')



main()



