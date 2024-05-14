eng = int(input())
ger = int(input())
fre = int(input())
match = set()
first = set()
second = set()
third = set()
for i in range(eng + ger + fre):
    name = input()
    if name in second:
        third.add(name)
    elif name in first:
        second.add(name)
    else:
        first.add(name)
result = (len(second) - len(third))
if result > 0:
    print(result)
else:
    print('NO')