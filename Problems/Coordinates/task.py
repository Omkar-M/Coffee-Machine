x = float(input())
y = float(input())
print("I" if x > 0 and y > 0
      else "II" if x < 0 < y
      else "IV" if y < 0 < x
      else "III")
