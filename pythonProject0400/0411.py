av = 0
s = 0
for i in range(int(input())):
    a = int(input())
    s += a
    av = s/(i+1)
    if a == av:
        print(0)
    elif a > av:
        print('>')
    else:
        print('<')