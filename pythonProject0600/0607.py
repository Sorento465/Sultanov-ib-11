my_set = []
n = int(input())
for i in range(n):
    s = set()
    for j in range(int(input())):
        sur = input()
        s.add(sur)
    my_set.append(s)
for i in range(n-1):
    f = (my_set[i] & my_set[i + 1])
    my_set[i+1] = f
for j in my_set[-1]:
    print(j)