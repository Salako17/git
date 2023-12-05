while True:
    fuel = input('FRACTION: ')
    if '/' in fuel:
        first, last = fuel.split('/')
        try:
            result = int(first) / int(last)
            result = result * 100
            if result <= 0:
                print('E')
            elif result > 1 and result < 98:
                print(f'{fuel}\n{round(result)}%', end='')
            elif result >= 99:
                print('F')
            
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except NameError:
            pass
        
        