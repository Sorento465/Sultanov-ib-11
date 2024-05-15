numbs = [int(a) for a in input().split()]
x, y = [int(b) for b in input().split()]
print(sum(numbs[x: y + 1]))