a = []
for i in range(int(input()[1:])):
    b = str(input())
    if '#' in b:
        b = ''.join(b[:b.index('#')])
    a.append(b)
for i in range(len(a)):
    print(a[i].rstrip())