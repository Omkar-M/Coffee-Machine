phrase = input()
new = str('')
for char in phrase:
    if char.isupper():
        char = '_' + char.lower()
    new += char
print(new)
