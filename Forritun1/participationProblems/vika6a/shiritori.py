inntak = input().lower()
allowed_words = inntak
banned_words = ""
inntak = input().lower()
while inntak != 'x':
    if inntak[0] == allowed_words[-1]:
        allowed_words += (" " + inntak)
    else:
        banned_words += inntak + " "
    inntak = input().lower()

print(allowed_words)
print(banned_words)