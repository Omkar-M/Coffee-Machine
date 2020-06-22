list__ = []
while True:
    x = input()
    if x != '.':
        x = float(x)
        list__.append(x)
    else:
        print(min(list__))
        break
