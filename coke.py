amounts_due = 50

coins = (5, 15, 25)
    
while amounts_due > 0:
    print(f'Amount_due: {amounts_due}')
    coin = int(input('Insert_coin: '))
    if coin in coins:
        amounts_due = amounts_due - coin
print(f'Change owed: {abs(amounts_due)}')


    