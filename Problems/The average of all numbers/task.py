a = int(input())
b = int(input())
sum_ = 0
count = 0
for x in range(a, b + 1, 1):
    if x % 3 == 0:
        count += 1
        sum_ += x
print(sum_ / count)
