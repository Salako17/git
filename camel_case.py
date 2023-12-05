message = input('enter name: ')

for char in message:
    if char.isupper():
        message = message.replace(char, "_" + char)
print(message.lower())
    









