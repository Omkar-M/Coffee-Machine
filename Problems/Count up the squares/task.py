sum_ = 0
sum_of_square = 0
while True:
    x = int(input())
    sum_ += x
    sum_of_square += x * x
    if sum_ == 0:
        break
print(sum_of_square)
