no1 = float(input())
no2 = float(input())
operator = input()
if operator == '+':
    print(no1 + no2)
elif operator == '-':
    print(no1 - no2)
elif operator == '/':
    if no2 == 0:
        print('Division by 0!')
    else:
        print(no1 / no2)
elif operator == '*':
    print(no1 * no2)
elif operator == 'mod':
    if no2 == 0:
        print('Division by 0!')
    else:
        print(no1 % no2)
elif operator == 'pow':
    print(no1 ** no2)
else:
    if no2 == 0:
        print('Division by 0!')
    else:
        print(no1 // no2)
