offset = input()
cal = 1030 + int(offset) * 100
if 0 < cal < 2400:
    print('Tuesday')
elif cal < 0:
    print('Monday')
else:
    print('Wednesday')
