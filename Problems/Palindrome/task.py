word = input()
index1 = -1
con = 1
for x in word:
    if x == word[index1]:
        index1 -= 1
    else:
        con = 0
        break
print('Palindrome' if con == 1 else 'Not palindrome')
