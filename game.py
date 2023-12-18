import random

while True:
    try:
        user_level = int(input('Enter the level: '))
        if user_level <= 0:
            continue
        while True:
            try:
                user_guess = int(input('Enter your guess: '))
                if user_guess > 0:
                    break
                else:
                    continue
            except ValueError:
                pass
                
        rand = random.randint(1, user_level)
        if rand == user_guess:
                print('You are right!')
        elif user_guess < rand:
            print('Too small. Try again.')
        else:
            print('Too large. Try again.')
        break            
            
    except ValueError:
        pass