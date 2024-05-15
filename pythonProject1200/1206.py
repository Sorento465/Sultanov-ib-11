s = input().upper()
for i in range(len(s) - 1):
    if s[i] != ' ' and s[i + 1] != '':
        print(f'{s[i]}-', end='')
    else:
        print(s[i], end='')
print(s[-1])