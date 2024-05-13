count = 0
summa = 0
a = 0
num = int(input())
while num != 0:
    if num == 0:
        break
    count += 1
    summa += num
    if summa == 10:
        a += count
    num = int(input())
print(a)