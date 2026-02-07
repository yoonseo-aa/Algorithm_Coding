word = input()
    
for w in word:
    if w.isupper(): print(w.lower(),end='')
    else: print(w.upper(),end='')