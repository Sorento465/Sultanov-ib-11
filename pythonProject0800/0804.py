num = int(input())
for i in range(num, 0, -1):
    for j in range(num):
        char = chr(ord('A') + j)
        print(char + str(i), end=' ')
    print()