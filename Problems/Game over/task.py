scores = input().split()
correct = 0
incorrect = 0
for x in scores:
    if x == 'C':
        correct += 1
    elif x == 'I':
        incorrect += 1
    if incorrect == 3:
        print('Game over')
        print(correct)
        break
else:
    print('You won')
    print(correct)
