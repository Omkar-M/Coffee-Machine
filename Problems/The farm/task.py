money = int(input().strip())

sheep = money // 6769
cow = money // 3848
pig = money // 1296
goat = money // 678
chicken = money // 23

if sheep:
    print(sheep, 'sheep')
elif cow:
    print(cow, 'cows' if cow > 1 else 'cow')
elif pig:
    print(pig, 'pigs' if pig > 1 else 'pig')
elif goat:
    print(goat, 'goats' if goat > 1 else 'goat')
elif chicken:
    print(chicken, 'chickens' if chicken > 1 else 'chicken')
else:
    print('None')
