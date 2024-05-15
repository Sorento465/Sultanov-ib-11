first = []
second = []
for i in range(int(input())):
    first.append(input())
for i in range(int(input())):
    second.append(input())
for first1 in first:
    for second2 in second:
        if first1 == second2:
            print(first1)