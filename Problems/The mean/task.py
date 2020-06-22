sum_ = 0
n = 0
while True:
    x = input()
    if x != '.':
        n += 1
        sum_ += int(x)
    else:
        break
print(sum_ / n)
