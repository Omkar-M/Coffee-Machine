hours = int(input())
if hours < 2:
    print('That seems reasonable')
else:
    print('Do you have time for anything else?' if hours < 4 else 'You need to get outside more!')
