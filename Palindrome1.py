word="racecar"
is_palindrome=True
for i in range(len(word)//2):
    if word[i]!=word[-(i+1)]:
        is_palindrome=False
        break
print(is_palindrome)
