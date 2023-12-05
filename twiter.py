letter = ['a', 'e', 'i', 'o', 'u']
names = input('what: ').lower()

for name in names:
    if name in letter:
        names = names.replace(name, "")
print(names)







