for x in range(1, 101):
    a = (x % 3 == 0)
    b = (x % 5 == 0)
    print("FizzBuzz" if a and b else "Fizz" if a else "Buzz" if b else x)
