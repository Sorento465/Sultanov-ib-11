a = set()
b = set()
c = input()
while c != '':
    a.add(c)
    c = input()
a.add(c)
d = input()
while d != '':
    b.add(d)
    d = input()
match = a & b
if not match:
    print('EMPTY')
else:
    for i in match:
        print(i)