a = set()
b = set()
N = int(input())
k = 0
for i in range(N):
    c = input()
    if not c in a:
        a.add(c)
        b.add(c)
    elif c in b:
        k += 2
        b.remove(c)
    else:
        k += 1
print(k)