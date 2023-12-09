import emoji
user = input('input: ')
try:
    print('hello,',emoji.emojize(user, language='alias'))
except:
    print('hello,',emoji.emojize(user))
