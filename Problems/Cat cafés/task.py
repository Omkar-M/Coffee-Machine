cafe = input().split()
max_cats, winner = 0, ''
while cafe[0] != 'MEOW':
    if int(cafe[1]) > max_cats:
        max_cats = int(cafe[1])
        winner = cafe[0]
    cafe = input().split()
print(winner)
