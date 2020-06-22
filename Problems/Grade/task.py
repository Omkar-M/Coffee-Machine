student_score = int(input())
max_score = int(input())

result = student_score / max_score * 100

if result >= 90:
    print('A')
elif result >= 80:
    print('B')
elif result >= 70:
    print('C')
elif result >= 60:
    print('D')
elif result < 60:
    print('F')
