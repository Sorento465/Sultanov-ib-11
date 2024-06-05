slov = {}
m = ''
sp, data, sort = [], [], []
for _ in range(int(input())):
    sp = input().split(' ')
    if sp[-1] not in data:
        data.append(sp[-1])
        slov[sp[-1]] = sp[0]
    else:
        sort = slov.get(sp[-1]).split(' ')
        sort.append(sp[0])
        sort.sort()
        m = ' '.join(sort)
        slov[sp[-1]] = m
    sp.clear()
for _ in range(int(input())):
    print(slov.get(input(), ''))