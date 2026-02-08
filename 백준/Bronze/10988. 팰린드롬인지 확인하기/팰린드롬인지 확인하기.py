def is_palindrome(word):
    if word == word[::-1]: return 1
    else: return 0
    
word = input()
result = is_palindrome(word)
print(result)