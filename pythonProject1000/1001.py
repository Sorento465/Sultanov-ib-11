numbs = []
answer = False
for i in range(int(input())):
    numbs.append(int(input()))
num = int(input())
for i in range(1, len(numbs)):
    for j in range(i):
        if num == numbs[i] * numbs[j]:
            answer = True
            break
if answer:
    print('ДА')
else:
    print('НЕТ')