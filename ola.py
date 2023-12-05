def main():
    machine = 50
    users = [1234, 2222, 4563, 3333, 4444]
    input = input('Enter your account number')
    if input in users:
        while machine > 0:
            print('Your account balance is', machine)
            print('_____________________What transaction do you want to perform____________________')
            print('Withdraw', 'Deposit', 'Statement of account')
            bank = input('ENTER ANY TRANSACTION YOU WISH TO PEFORM: ').lower()
            if bank == 'withdraw':
                user_input = int(input('How do you want to withdraw: '))
                machine = machine - user_input
                print(abs(machine))
            elif bank == 'deposit':
                user_input = int(input('How do you want to depodit: '))
                machine = machine + user_input
                print(abs(machine))
            elif bank == 'statement of account':
                
                print(abs(machine))

main()



    