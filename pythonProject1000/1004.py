text = []
for i in range(int(input())):
    text.append(input())
correct = sorted(text, key = len)
for cor in correct:
    print(cor)