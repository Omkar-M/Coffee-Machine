text = input()
con = 'aeiou'
non = '#@! ?.,;'
for x in text:
    if x in con:
        print('vowel')
    elif x in non:
        break
    else:
        print('consonant')
