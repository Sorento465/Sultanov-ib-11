text = input()
m = 0
n = 0
for i in range(len(text)):
    if text[i] != 'p':
        n += 1
    elif text[i] == 'p':
        n = 0
    if n > m:
        m = n
print(m)