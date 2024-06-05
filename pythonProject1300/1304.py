n = int(input('n = '))
d = {}
for _ in range(n):
    x,y = map(int, input('x, y->').split())
    d.setdefault((x//10,y//10), 0)
    d[(x//10,y//10)] += 1
print(max(d.values()))