text = []
for i in range(int(input())):
    text.append(input())
n = int(input())
k = int(input())
for i in range(len(text)):
    if (i + 1) % n:
        print(text[i])