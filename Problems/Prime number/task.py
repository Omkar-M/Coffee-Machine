def isprime(x):
    if x < 2:  # negative numbers, 0 and 1 are not prime
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True


if isprime(int(input())):
    print("This number is prime")
else:
    print("This number is not prime")
